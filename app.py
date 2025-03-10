import streamlit as st
import joblib
import numpy as np

# Загружаем модель
model = joblib.load("model.pkl")

# Заголовок веб-приложения
st.title("Прогнозирование спроса с RandomForestRegressor")

st.write("Введите параметры для предсказания:")

# Поля для ввода признаков
season = st.selectbox("Сезон (1 - весна, 2 - лето, 3 - осень, 4 - зима)", [1, 2, 3, 4])
holiday = st.selectbox("Праздничный день (0 - нет, 1 - да)", [0, 1])
workingday = st.selectbox("Рабочий день (0 - нет, 1 - да)", [0, 1])
temp = st.number_input("Температура (°C)", value=20.0)
dew_point = st.number_input("Точка росы (°C)", value=10.0)
humidity = st.number_input("Влажность (%)", value=50.0)
wind_speed = st.number_input("Скорость ветра (м/с)", value=5.0)
hour = st.slider("Час (0-23)", 0, 23, 12)
day = st.slider("День месяца (1-31)", 1, 31, 15)
month = st.slider("Месяц (1-12)", 1, 12, 6)
year = st.slider("Год (например, 2023)", 2020, 2030, 2023)
day_of_week = st.selectbox("День недели (0 - Пн, ..., 6 - Вс)", list(range(7)))

# Кнопка предсказания
if st.button("Сделать предсказание"):
    input_data = np.array([[season, holiday, workingday, temp, dew_point, humidity,
                             wind_speed, hour, day, month, year, day_of_week]])
    prediction = model.predict(input_data)
    st.success(f"Предсказанное значение: {float(prediction[0, 0]):.2f}")