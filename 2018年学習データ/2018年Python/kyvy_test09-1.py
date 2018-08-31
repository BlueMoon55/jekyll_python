# coding: utf -8
# クラス定義
class Person:
    # クラス変数
    population = 7400000000
    # コンストラクタ
    def __init__(self ,Name ,Age ,Gender ,Country ):
        self.name = Name
        self.age = Age
        self.gender = Gender
        self.country = Country
    # クラスメソッド
    @classmethod
    def belongTo(cls):
        print(cls ,'は人類に属しています． ')
        return 'Human '
    # メソッド
    def getName(self ):
        print('名前は', self.name ,'です． ')
        return self.name
    def getAge(self ):
        print('年齢は', self.age ,'才です． ')
        return self.age
    def getGender(self ):
        print('性別は', self.gender ,'性です． ')
        return self.gender
    def getCountry(self ):
        print(self.country ,'から来ました． ')
        return self.country

# メインルーチン
m1 = Person('太郎',39,'男','日本')
m2 = Person('アリス',28,'女','アメリカ')

m1.getName ()
m1.getAge ()
m1.getGender ()
m1.getCountry ()

m2.getName ()
m2.getAge ()
m2.getGender ()
m2.getCountry ()

Person.belongTo ()
print('現在の人口は約', Person.population ,'人です． ')
