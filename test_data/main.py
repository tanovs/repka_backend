from goods.good import AddGood, AddGoodRequest
import requests

def get_good_data_vkusnie_istoryy():
    name = ["Мусс творожный фруктово - ягодный (клубника-манго), 130г", "Смузи Боул Ананас, Банан, Кокос, 120г", "СМУЗИ боул манго, маракуйя, кокос, 120 г", "Желе фруктово-ягодное(арбуз, дыня), 160г", "Чиа светофор, 90г", "Мусс Кокосовый 110г", "Мусс шоколадно-карамельный 120г", "Фруктовый микс Манго, Клубника, 140г", "Мусс карамельный, 120г", "Микс Манго, Голубика 200г", "Ананас Кубики, 300г", "Ананас целый, 400г", "Ананас Полукольца, 300г", "Гранат Зерна, 120г", "Фруктовый микс манго, клубника, голубика 400г", "Фруктовый микс ананас, клубника, голубика 400г"]
    price = ["р.168,00", "р.138,00", "р.136,00", "р.133,00", "р.137,50", "р.139,00", "р.137,50", "р.163,50", "р.132,00", "р.243,00", "р.342,00", "р.430,30", "р.360,00", "р.169,18", "р.486,00", "р.476,00"]
    volume = ["130г", "120г", "120г", "160г", "90г", "110г", "120г", "140г", "120г", "200г", "300г", "400г", "300г", "120г", "400г", "400г"]
    calories = ["161", "188,1", "139,8", "46,9", "198", "357", "333,4", "57,3", "465,6", "57", "52", "52", "52", "72", "60,5", "46,2"]
    compound = ["манго свежее, сливки питьевые м.д.ж. 33% (сливки нормализованные), творог мягкий обезжиренный(молоко обезжиренное пастеризованное с использованием закваски. Технологическое средство: ферментный препарат животного происхождения пепсин, химозин.), йогурт питьевой (нормализованное молоко, восстановленное молоко из сухого молока, йогуртовая закваска, бифидобактерии B.Lactis), cахар, клубника свежая, вода, семена чиа, желатин говяжий,ванильная паста (сахар, глюкозный сироп, обезжиренное сгущенное молоко, ванильный экстракт, натуральный ароматизатор (ваниль), мадагаскарские ванильные бобы, крахмал, растительные экстракты). Продукт может содержать следы орехов.",
                "кокосовые «сливки» (мякоть кокосового ореха 90%, вода 9,9%, стабилизаторы (ксантановая камедь, гуаровая камедь) 0,1%), банан, ананас, ксантановая камедь, натуральный экстракт ванили, кокосовое масло, голубика, семена чиа, кокосовая стружка.",
                "яблоко, Ананас, Банан, манго, Пюре Манго, Сахар, Кокосовые Сливки, Кокосовое Молоко, Пюре Маракуйя, Кокосовое Масло, Голубика, Кокос, Ксантановая Камедь, Семена Чиа, Цедра Лайма, Ванильная Паста",
                "Вода, арбуз, дыня, сахар, вода, желатин, Лимонная Кислота, Ароматизатор натуральный дыня", "Кокосовое Молоко, вода, Семена Чиа, фруктоза, манго, киви, клубника, Ванильная Паста",
                "Сливочное масло 72,5%, сахар, сухой желток, сухой белок, вода, кокосовые сливки, пшеничная мука, разрыхлитель, мелкая кокосовая стружка, кукурузный крахмал,молоко 2,5%, сливки 33%, соль,ванилин, клубника, миндальная крошка",
                "сливки 33%, сахар, масло сливочное 72,5%, мед, голубика, мука пшеничная, какао, инвертный сахарный сироп, белок яичный сухой, вода, желатин, соль, ванильная паста, сода питьевая, кофе сублимированный растворимый.",
                "Манго, клубника", "арахис жареный, молоко 2,5%, сливки 33%, масло сливочное 72,2%, инвертный сахарный сироп, клубника, голубика, вафельная крошка, шоколад молочный, яичный сухой белок, желатин, вода, подсолнечное масло, мука пшеничная, какао масло, какао, разрыхлитель, соль.",
                "Манго, голубника", "Ананас", "Ананас", "Ананас", "Гранат", "манго, клубника, голубика", "ананас, клубника, голубика"]
    expiration_day = ["4", "4", "4", "7", "4", "7", "7", "4", "7", "5", "7", "7", "4", "4", "4", "4"]
    brand = "FresCo"
    supplier_id = "3803a670-77c9-43be-81a8-f2945c0a1e1b"
    tag_id = [
        "5a05897b-8556-497f-99b6-ed6defe9b915",
        "3f358003-29e5-4670-92be-46ff8f6826e9",
        "3f358003-29e5-4670-92be-46ff8f6826e9",
        "4a370466-8892-4f38-b11c-b00c88edea87",
        "4a370466-8892-4f38-b11c-b00c88edea87",
        "4a370466-8892-4f38-b11c-b00c88edea87",
        "4a370466-8892-4f38-b11c-b00c88edea87",
        "db688434-9a5f-4bdb-a5e1-0c51ba7230fb",
        "4a370466-8892-4f38-b11c-b00c88edea87",
        "db688434-9a5f-4bdb-a5e1-0c51ba7230fb",
        "05effc36-5b12-49f1-a7ef-052819c3be80",
        "05effc36-5b12-49f1-a7ef-052819c3be80",
        "05effc36-5b12-49f1-a7ef-052819c3be80",
        "3662cff1-ca4b-4963-a4ae-0bae95945f46",
        "db688434-9a5f-4bdb-a5e1-0c51ba7230fb",
        "3662cff1-ca4b-4963-a4ae-0bae95945f46",
    ]
    body = AddGoodRequest(supplier_id=supplier_id, goods=[])
    for i in range(0, 16):
        good = AddGood(
            name = name[i],
            price = price[i],
            volume = volume[i],
            calories = calories[i],
            compound = compound[i],
            expiration_day = expiration_day[i],
            producer = brand,
            tag_id = tag_id[i],
            balance=0,
        )
        body.goods.append(good)
    return body


def get_good_data_zagotprom():
    name = ["Полуфабрикат концентрированного морса стандарт клюквенный (2 кг.)", "Полуфабрикат концентрированного морса стандарт черносмородиновый (2 кг.)", "Полуфабрикат концентрированного морса стандарт облепиховый (2 кг.)", "Черника замороженная (10кг)", "Пюре фруктовое, консервированное асептическим способом (клюква) (2 кг.)"]
    price = ["р.290,00", "р.290,00", "р.290,00", "р.280,00", "р.420,00"]
    volume = ["200кг", "200кг", "200кг", "500кг", "200кг"]
    calories = ["207; 0,5; 0; 53,7", "215; 0,6; 0,2; 57,3", "234; 1,2; 5,4; 55,7", "57; 0,74; 0,33; 12,09", "28; 05; 0; 3,1"]
    compound = ["Клюква, сахар", "Черная смородина, сахар", "Облепиха, сахар", "Черника", "Клюква"]
    expiration_day = "12 мес"
    brand = "Zagotprom"
    supplier_id = "230cba86-f5b1-4577-a655-5befd14b17d5"
    tag_id = [
        "33eff0fa-796f-4a20-92b2-8b030be56d49",
        "33eff0fa-796f-4a20-92b2-8b030be56d49",
        "33eff0fa-796f-4a20-92b2-8b030be56d49",
        "504786fa-d4c0-4946-bcca-3301593ceb19",
        "3f358003-29e5-4670-92be-46ff8f6826e9",
    ]
    body = AddGoodRequest(supplier_id=supplier_id, goods=[])
    for i in range(0, 5):
        good = AddGood(
            name = name[i],
            price = price[i],
            volume = volume[i],
            calories = calories[i],
            compound = compound[i],
            expiration_day = expiration_day,
            producer = brand,
            tag_id = tag_id[i],
            balance=0,
        )
        body.goods.append(good)
    return body

def get_good_data_ferro():
    name = ["Спагетти №9", "Спагетти №12", "Тальятелле", "Казаречче", "Папарделле", "Лингвини", "Маккерони", "Фузилли", "Ньокки картофельные", "Цветная паста с натуральными красителями"]
    price = ["р.380,00", "р.380,00", "р.380,00", "р.380,00", "р.380,00", "р.380,00", "р.380,00", "р.380,00", "р.380,00", "р.420,00"]
    volume = "1 кг"
    balance = "400 г"
    compound = "Мука из твёрдых сортов пшеницы (семола), вода питьевая минерализованная, яйцо куриное пастеризованное, соль морская."
    expiration_day = "от 14 до 30 суток (+2..+4)"
    brand = "Ferro"
    supplier_id = "8b364ef5-cb96-4f88-a639-6e423fec60d1"
    tag_id = "86b3eba0-bc78-4eee-8caa-83b8e79418da"
    body = AddGoodRequest(supplier_id=supplier_id, goods=[])
    for i in range(0, 5):
        good = AddGood(
            name = name[i],
            price = price[i],
            volume = volume,
            compound = compound,
            expiration_day = expiration_day,
            producer = brand,
            tag_id = tag_id,
            balance=balance,
        )
        body.goods.append(good)
    return body

def get_good_data(data_type: str):
    tmp = {
        'vkusnie_istoryy': get_good_data_vkusnie_istoryy,
        'zagotprom': get_good_data_zagotprom,
        'ferro': get_good_data_ferro,
    }
    return tmp[data_type]()

def main():
    companies = ['vkusnie_istoryy', 'zagotprom', 'ferro']
    for company in companies:
        goods = get_good_data(company)
        print(goods.json())
        result = requests.post('http://127.0.0.1:8080/api/v1/good/add', data=goods.json())
        print(result.json(), result.status_code)
        

if __name__ == '__main__':
    main()