from mymedi import db


# 유저 모델 속성
# id: 유저 데이터의 고유 번호
# sub: 구글 로그인한 유저의 고유 값
# fullname: 유저 이름
# birthday: 유저 생년월일
# gender: 유저 성별

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sub = db.Column(db.String(250), unique=True, nullable=False)
    fullname = db.Column(db.String(100), nullable=False)
    birthday = db.Column(db.DateTime(), nullable=False)
    gender = db.Column(db.String(20), nullable=False)