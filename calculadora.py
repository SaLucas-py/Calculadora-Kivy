from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.uix.widget import Widget


Window.size = (500,700)



class MyBoxLayout(Widget):
   
    def clear(self):
        self.ids.calc_input.text='0'

    def button_press(self, button):
        prior = self.ids.calc_input.text
        if prior == '0':
            self.ids.calc_input.text = ''
            self.ids.calc_input.text = f'{button}'
        else:
            self.ids.calc_input.text = f'{prior}{button}'
  
    
    def add(self):
        prior = self.ids.calc_input.text
        self.ids.calc_input.text = f'{prior}+'
    def sub(self):
        prior = self.ids.calc_input.text
        self.ids.calc_input.text = f'{prior}-'

    def mult(self):
        prior = self.ids.calc_input.text
        self.ids.calc_input.text = f'{prior}*'
    def div(self):
        prior = self.ids.calc_input.text
        self.ids.calc_input.text = f'{prior}/'
    def math_sign(self, sign):
        prior = self.ids.calc_input.text
        self.ids.calc_input.text = f'{prior}{sign}'
       
    def equals(self):
        prior = self.ids.calc_input.text
        
        if '+' in prior:
            num_list = prior.split('+')
            answer = 0

            for number in num_list:
                answer = int(number) + answer
            self.ids.calc_input.text = str(answer)
            

        if '-' in prior:
            num_list = prior.split('-')
            answer = 0
            
            for number in num_list:
                answer = -int(number) - answer
            self.ids.calc_input.text = str(answer)

        if '*' in prior:
            num_list = prior.split('*')
            answer = 1
            
            for number in num_list:
                answer = int(number) * answer
            self.ids.calc_input.text = str(answer)


        if '/' in prior:
            num_list = prior.split('/')
            answer = 1
        
            for number in num_list:
                answer = int(num_list[0]) / int(num_list[1])
                print('esse eh o number: {}'.format(number))
                print(answer)
            self.ids.calc_input.text = str(answer)

            


        

            
            

            
            
        
        



class MainApp(App):
    def build(self):
        return MyBoxLayout()

    

MainApp().run()