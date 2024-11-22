# Python Проект
## Описание проекта
Мой проект это игра, текстовый квест, в котором игрок выбирает из предложенных вариантов ответа, в игре присутствует сюжет по которому игрок продвигается в зависимости от выбора

Также присутствуют жизни игрока, когда они заканчиваются, то и игра заканчивается, некоторое выборы прибавляют жизни, некоторые выборы убирвют жизни

## Реализуемый функционал
Основная механика это выбор из предложенных вариантов ответов. То есть игра предлагает несколько действий и описание ситуации.

На экране пользователь видит несколько кнопок, при нажатии на которые игровой персонаж выполняет действия написанные на кнопках. Также на экране есть текст с описанием ситуации в игровом мире в данный момент.

Фоновая картинка отражает место в котором внутри игры находится персонаж. Присутствует музыка.

Еще реализована механика жизней игрока, количество которых будет меняться от выборов игрока. Изначально дано три жизни и их количество может как увеличиваться, так и уменьшаться.

## Архитектура

Реализована большая часть будет с помощью библиотеки pygame.

#### Кнопки
За кнопки будет отвечать отдельный класс, при инициализации экземпляра класса задается размер кнопки, место на экране, текст и картинки, при наведении мыши на кнопку картинка на ней меняется.

Также присутствуют методы прорисовки, определения наведена ли мышь и действий при нажатии.

#### Фон
За фон планируется создать отдельный класс, при инициализации он просто выводит первую фоновую картинку, будет присутствовать метод, который меняет картинку на следующую, где то будет хранится порядок вывода картинок.

Также в этот класс планируется добавить проигрывание фоновой музыки, которая не зависит от действий в игре.

#### Описание события
Это не кнопка, но по структуре похожа, то есть задается картинка, положение на экране, размеры и метод прорисовки, но нет метода менять при нажатии, будет добавлен метод, чтобы текст менялся на следующий.

Нужные текста тоже будут где то храниться.

#### Общий класс/функция игры
Наверное еще будет такой класс/функция, чтобы не выносить большую часть кода в основной файл, будет отвечать за порядок действий и общий вывод на экран тех или иных объектов.

Отвечать за смысловую часть сюжета игры.

#### Жизни
Класс отвечающий за механику жизней, аналогично задается расположение на экране и картинка. Методы прибавления и убавления.

## Запуск приложения

```bash
git clone https://github.com/Muravevm/Python_project

pip install -r requirements.txt

python3 main.py
```