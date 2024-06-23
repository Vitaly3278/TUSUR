import psycopg2
from psycopg2 import Error

try:
    connection = psycopg2.connect(user="postgres",
                                  password="1234",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="Case1")

    cursor = connection.cursor()

    query = """
    SELECT o.gender, o.education, o.contact_type, o.response_to_campaign, 
            l.city, l.country, c.has_credit_card, c.bank, c.offer_type,
            cs.card_number, cs.average_check, cs.current_balance, cs.credit, cs.number_of_cards
    FROM owners o
    JOIN owner_locations ol ON o.owner_id = ol.owner_id
    JOIN locations l ON ol.location_id = l.location_id
    JOIN cards c ON o.owner_id = c.owner_id
    JOIN card_statistics cs ON c.card_id = cs.card_stat_id
    LIMIT 50
    """

    cursor.execute(query)

    results = cursor.fetchall()

    for row in results:
        print(*row)


except (Exception, Error) as error:
    print("Ошибка при работе с PostgreSQL", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("Соединение с PostgreSQL закрыто")
