import justpy as jp


class Doc():

    def serve(self):
        wp = jp.WebPage()



        div = jp.Div(a=wp, classes = 'bg-gray-200 h-screen')

        jp.Div(a=div, text='Instant Dictionary API', classes='text-4xl n-2')
        jp.Div(a=div, text='Get the definition of words', classes='text-lg')
        jp.Hr(a=div)
        jp.Div(a=div, text='Use http://127.0.0.1:8000/api?w=moon to get the definition of word moon, change the word to get it\'s definition')
        jp.Hr(a=div)
        jp.Div(a=div, text="""
        {"word": "moon", 
        "definition": 
        ["A natural satellite of a planet.", 
        "A month, particularly a lunar month (approximately 28 days).", 
        "To fuss over adoringly or with great affection.", 
        "Deliberately show ones bare ass (usually to an audience, or at a place, where this is not expected or deemed appropriate).", 
        "To be lost in phantasies or be carried away by some internal vision, having temorarily lost (part of) contact to reality."]}
        """)
        return wp



