from flask import jsonify
from app.api import bp

@bp.route('/ping', methods=['GET'])
def ping():
  ''' 前端vue.js 用来测试与后端flask api的连通性 '''
  return jsonify('Bomm!')