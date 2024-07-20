import numpy as np
import pandas as pd
import streamlit as st
import joblib
from config import config


def round_to_hundred(price):
    return int(np.round(price / 100.0)) * 100


def remove_city(district, selected_city):
    return district.replace(f' ({selected_city})', '')


def append_city(district, selected_city):
    return district + f' ({selected_city})'


def main(model, df):

    user_selections = {
        'Поверх': None,
        'Поверховість': None,
        'Загальна площа': None,
        'Площа кухні': None,
        'Кількість кімнат': None,
        'Меблювання': None,
        'Ремонт': None,
        'Місто': None,
        'Район': None,
        'Підключене резервне живлення': None,
        'Працює ліфт': None,
    }

    st.title('Тайтл')

    # City dropdown
    city_options = df['Місто'].unique().tolist()
    city_options.sort()
    city_options.remove('Інше')
    city_options.insert(0, 'Інше')

    user_selections['Місто'] = st.selectbox(
        'Місто: ', city_options,
        placeholder="Виберіть місто"
    )

    # District dropdown
    district_options = df[df['Місто'] == user_selections['Місто']]['Район'].unique().tolist()
    user_selections['Район'] = 'Невідомо'
    if len(district_options) > 1:
        district_options.sort()
        if 'Невідомо' in district_options:
            district_options.remove('Невідомо')
            district_options.insert(0, 'Інший')
        district_options = [remove_city(district, user_selections['Місто']) for district in district_options]

        user_selections['Район'] = st.selectbox('Район: ', district_options, placeholder="Виберіть район")

        if user_selections['Район'] == 'Інший':
            user_selections['Район'] = 'Невідомо'
        else:
            user_selections['Район'] = append_city(user_selections['Район'], user_selections['Місто'])

    # Number of floors in the building
    user_selections['Поверховість'] = st.number_input(
        'Поверховість будинку: ',
        min_value=1,
        max_value=df['Поверховість'].max(),
        step=1,
        placeholder=""
    )

    # Floor number
    user_selections['Поверх'] = st.number_input(
        'Поверх: ',
        min_value=1,
        max_value=user_selections['Поверховість'] if user_selections['Поверховість'] else df['Поверх'].max(),
        step=1,
        placeholder=""
    )

    # Total area
    user_selections['Загальна площа'] = st.number_input(
        'Загальна площа (м²): ',
        min_value=0.0,
        step=0.01,
        placeholder=""
    )

    # Kitchen area
    user_selections['Площа кухні'] = st.number_input(
        'Площа кухні (м²): ',
        min_value=0.0,
        step=0.01,
        placeholder=""
    )

    # Number of rooms
    number_of_rooms_options = df['Кількість кімнат'].unique().tolist()
    number_of_rooms_options.sort()

    user_selections['Кількість кімнат'] = st.selectbox(
        'Кількість кімнат: ',
        number_of_rooms_options,
        placeholder=""
    )

    # Furniture
    user_selections['Меблювання'] = st.selectbox(
        'Наявність меблів: ',
        ['З меблями', 'Неважливо'],
        placeholder=""
    )

    # Repair
    repair_options = df['Ремонт'].unique().tolist()
    repair_options.remove('Не вказано')
    repair_options.insert(0, 'Неважливо')

    user_selections['Ремонт'] = st.selectbox(
        'Стан помешкання: ',
        repair_options,
        placeholder=""
    )
    user_selections['Ремонт'] = 'Не вказано' if user_selections['Ремонт'] == 'Неважливо' else user_selections['Ремонт']

    # Elevator
    user_selections['Працює ліфт'] = st.selectbox(
        'Наявність працюючого ліфту при блекаутах: ',
        ['Ні', 'Так'],
        placeholder=""
    )
    user_selections['Працює ліфт'] = 1 if user_selections['Працює ліфт'] == 'Так' else 0

    # Backup power in the house
    user_selections['Підключене резервне живлення'] = st.selectbox(
        'Наявність резервного живлення в будинку: ',
        ['Ні', 'Так'],
        placeholder=""
    )
    user_selections['Підключене резервне живлення'] = 1 if user_selections['Підключене резервне живлення'] == 'Так' else 0

    # Show predicted price
    if st.button('Вирахувати орієнтовну ціну'):
        prediction = model.predict(pd.DataFrame([user_selections]))
        price = np.exp(prediction)[0]
        st.title(f"Орієнтовна ціна: {round_to_hundred(price)} грн")


if __name__ == '__main__':

    with open(config.get_path('model_path'), 'rb') as file:
        model = joblib.load(file)

    with open(config.get_path('clean_data_path'), 'rb') as file:
        df = joblib.load(file)

    if model and (df is not None):
        main(model, df)