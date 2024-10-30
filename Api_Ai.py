from flask import Flask, request, jsonify
import pickle
import pandas as pd
import psycopg2
from dotenv import load_dotenv
from psycopg2 import OperationalError
import os

load_dotenv()

app = Flask(__name__)

def connect() -> psycopg2.extensions.connection:
    try:
        cnn = psycopg2.connect(
            host=os.getenv('HOST'),
            database=os.getenv('DBNAME'),
            user=os.getenv('USER'),
            password=os.getenv('PASSWORD'),
            port=int(os.getenv('DBPORT'))
        )
        return cnn
    except OperationalError as oe:
        print("Database connection error:", oe)
        return None

def disconnect(cnn):
    if cnn:
        cnn.close()
        
@app.route('/', methods=['GET', 'HEAD'])
def keep_alive():
    return '', 200

@app.route('/getResponse/', methods=['POST'])
def getResponse():
    try:
        body = request.get_json()

        missingCols = []
        requiredCols = ['email', 'nome_empresa', 'uf', 'porte_empresa', 'capital_social', 
                        'municipios', 'cnaes', 'natureza_juridica', 'ano_inicio_ativ', 
                        'mes_inicio_ativ', 'dia_inicio_ativ']
        for i in requiredCols:
            if i not in [k.lower() for k in body.keys()]:
                missingCols.append(i)

        if len(missingCols) > 0:
            return jsonify({'error': 'missing required columns', 'missing_columns': missingCols}), 400

        vals = [body['uf'], body['porte_empresa'], body['capital_social'], body['municipios'], 
                body['cnaes'], body['natureza_juridica'], body['ano_inicio_ativ'], 
                body['mes_inicio_ativ'], body['dia_inicio_ativ']]
        
        test = pd.DataFrame([vals], columns=['UF', 'Porte Empresa', 'Capital Social', 
                                             'municipios', 'cnaes', 'Natureza Juridica', 
                                             'ano inicio_ativ', 'mes inicio_ativ', 'dia inicio_ativ'])

        try:
            
            with open(rf'pipeline.pkl','rb') as f:
                pipeline = pickle.load(f)
        except Exception as e:
            return jsonify({'error': 'Failed to load prediction model', 'details': str(e)}), 500

        try:
            response = pipeline.predict(test)[0]
        except ValueError as ve:
            return jsonify({'error': 'Input data error', 'details': str(ve)}), 400
        except Exception as e:
            return jsonify({'error': 'Prediction execution failed', 'details': str(e)}), 500
        
        cnn = connect()
        if not cnn:
            return jsonify({'error': 'Database connection failed'}), 500

        try:
            cursor = cnn.cursor()
            cursor.execute(
                "INSERT INTO ia_tests(email, nome_empresa, uf, porte_empresa, capital_social, municipios, cnaes, "
                "natureza_juridica, ano_inicio_ativ, mes_inicio_ativ, dia_inicio_ativ, response) "
                "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                (body['email'], body['nome_empresa'], body['uf'], body['porte_empresa'], body['capital_social'], 
                 body['municipios'], body['cnaes'], body['natureza_juridica'], 
                 body['ano_inicio_ativ'], body['mes_inicio_ativ'], body['dia_inicio_ativ'], response)
            )
            cnn.commit()
        finally:
            cursor.close()
            disconnect(cnn)

        return jsonify({'response': response}), 200

    except Exception as ex:
        print("An error occurred:", ex)
        return jsonify({'error': 'An error occurred during processing', 'details':str(ex)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
