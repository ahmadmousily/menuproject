import PySimpleGUI as sg

sg.theme('SystemDefault')





def layout_create(x,items):
    if x == 1:
        layout =[
                [
                    sg.Button('تيركي', size=(12, 2), font=12),
                    sg.Button('روستبيف', size=(12, 2), font=12),
                    sg.Button('تونا', size=(12, 2), font=12)
                ],

                [
                    sg.Button('يلنجي صغير', size=(12, 2), font=12),
                    sg.Button('يلنجي كبير', size=(12, 2), font=12),
                    sg.Button('تبولة', size=(12, 2), font=12),

                ],

                [
                    sg.Button('بطاطا', size=(12, 2), font=12),
                    sg.Button('تيندرز', size=(12, 2), font=12),
                    sg.Button('بروتين بودنج', size=(12, 2), font=12),
                ],
                [
                    sg.Button('معكرونة', size=(12, 2), font=12)
                ],
                [sg.Button('Back', key='back1', size=(12, 2), font=12, button_color='black')]
            ]
    if x == 2:
        layout= [
            [
                sg.Button('قهوة تركية', size=(12, 2), font=12),
                sg.Button('قهوة اميريكان', size=(12, 2), font=12),
                sg.Button('شاي', size=(12, 2), font=12)], [
                sg.Button('شاي أخضر', size=(12, 2), font=12),
                sg.Button('نسكافيه', size=(12, 2), font=12),
                sg.Button('في ايس', size=(12, 2), font=12)],
            [
                sg.Button('فيمتو', size=(12, 2), font=12),
                sg.Button('عصير مراعي', size=(12, 2), font=12),
                sg.Button('عصير بلدنا', size=(12, 2), font=12)],
            [sg.Button('ايس تي', size=(12, 2), font=12),
             sg.Button('ماء', size=(12, 2), font=12),
             sg.Button('زهورات', size=(12, 2), font=12)],
            [sg.Button('أميريكان مع حليب', size=(12, 2), font=12),
             ],
            [sg.Button('Back', key='back2', size=(12, 2), font=12, button_color='black')]
        ]

    if x == 3:
        layout=[
            [
            sg.Button('شيس بليس',size=(12,2),font=12),
            sg.Button('شبس سنبس',size=(12,2),font=12),
            sg.Button('كيك',size=(12,2),font=12)
            ],
            [
            sg.Button('شبس تشيتوس', size=(12, 2), font=12),
            sg.Button('بروتين بار',size=(12,2),font=12),
            sg.Button('فورنو',size=(12,2),font=12)
            ],
            [
            sg.Button('علكة',size=(12,2),font=12),
            sg.Button('سنبايتس',size=(12,2),font=12)
            ],
            [sg.Button('Back',key='back3',size=(12,2),font=12,button_color='black')]
        ]
    if x == 4:
        layout = [[sg.Listbox(items,size=(40,20))]]
    return layout

layout=[
    [
        sg.Button('مأكولات',size=(12,2),font=12,key=1),
        sg.Button('مشروبات',size=(12,2),font=12,key=2),
        sg.Button('سناكس',size=(12,2),font=12,key=3)],
    [
        sg.Button('complete order',size=(12,2),font=12,key='complete')
    ]

    ]

window= sg.Window('Menu',layout)
items=[ ]
while True:

    event, values = window.read()
    print(event,values)

    if event == sg.WINDOW_CLOSED:
        break
    if event == 1:
        window.hide()
        window_food= sg.Window('Food',layout_create(1,items))
        while True:
            event1,values1 = window_food.read()
            if event1 == sg.WINDOW_CLOSED:
                break
            if event1 == 'back1':
                window_food.close()
                window.un_hide()
            if event1 != []:
                if event1 != 'back1':
                    items.append(event1)
    if event == 2:
        window.hide()
        window_drinks = sg.Window('Drinks', layout_create(2))
        while True:
            event2, values2 = window_drinks.read()
            if event2 == sg.WINDOW_CLOSED:
                break
            if event2 == 'back2':
                window_drinks.close()
                window.un_hide()
    if event == 3:
        window.hide()
        window_snacks = sg.Window('Snacks', layout_create(3))
        while True:
            event3, values3 = window_snacks.read()
            if event3 == sg.WINDOW_CLOSED:
                break
            if event3 == 'back3':
                window_snacks.close()
                window.un_hide()

    if event == 'complete':
        window.close()
        window_result= sg.Window('bill',layout_create(4,items))
        while True:
            event_final,values_final=window_result.read()
            if event_final == sg.WINDOW_CLOSED:
                break





window.close()