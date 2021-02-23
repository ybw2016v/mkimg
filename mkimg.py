from flask_restful import reqparse , Api, Resource
from flask import Flask, request
from flask import jsonify
import psycopg2
from dbdog import get_dog_id,write_dog_pic
from dogfile import DogFile
import os
from initdbdog import get_dog_instance_info

dogyml=os.getenv('MISSKEY_YML_PATH')

dogdbi=get_dog_instance_info(dogyml)


app = Flask(__name__)
app.config.update(RESTFUL_JSON=dict(ensure_ascii=False))
api = Api(app)

app.config['JSON_AS_ASCII'] = False

parser = reqparse.RequestParser()
parser.add_argument('i', type=str, help='token')
parser.add_argument('url', type=str, help='url')

pgdog = psycopg2.connect(database=dogdbi[2], user=dogdbi[3],password=dogdbi[4], host=dogdbi[0], port=dogdbi[1])

class imgdog(Resource):
    def get(self):
        idog = request.args.get("i")
        urldog = request.args.get("url")
        if idog is None:
            return {'r':'bad'}
        iddog=get_dog_id(pgdog,idog)
        if iddog is None:
            return {'r':403}
        try:
            dogf=DogFile(urldog)
        except:
            return {'r':500}
        if dogf.dogtype !='other':
            write_dog_pic(pgdog,dogf,iddog)
            return {'r':'success','id':iddog,'pid':dogf.id}
        return {'r':'?'}

    def post(self):
        args = parser.parse_args()
        idog = args["i"]
        urldog = args["url"]
        if idog is None:
            return {'r':'bad'}
        iddog=get_dog_id(pgdog,idog)
        if iddog is None:
            return {'r':403}
        try:
            dogf=DogFile(urldog)
        except:
            return {'r':500}
        if dogf.dogtype !='other':
            write_dog_pic(pgdog,dogf,iddog)
            return {'r':'success','id':iddog,'pid':dogf.id}
        return {'r':'?'}

api.add_resource(imgdog, '/')

if __name__ == '__main__':
    app.run(debug=True)