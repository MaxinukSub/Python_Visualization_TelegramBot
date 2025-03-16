from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from aiogram.utils.keyboard import InlineKeyboardBuilder

def create_plot():
    inline_kb_list = [
        [InlineKeyboardButton(text="Круговая диаграмма", callback_data='draw_pie')],
        [InlineKeyboardButton(text="Диаграмма рассеивания", callback_data='draw_scatterPlot')],
        [InlineKeyboardButton(text="Столбчатая диаграмма", callback_data='draw_barPlot')],
        [InlineKeyboardButton(text="Гистограмма", callback_data='draw_histPlot')],
        [InlineKeyboardButton(text="Назад", callback_data='back_to_start')]
    ]
    return InlineKeyboardMarkup(inline_keyboard=inline_kb_list)