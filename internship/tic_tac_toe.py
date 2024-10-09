from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class TicTacToeGrid(BoxLayout):
    def __init__(self, **kwargs):
        super(TicTacToeGrid, self).__init__(**kwargs)
        self.orientation = 'vertical'

        self.status_label = Label(text="Player X's turn", size_hint=(1, 0.1))
        self.add_widget(self.status_label)

        self.grid_layout = GridLayout(cols=3)
        self.buttons = [[None for _ in range(3)] for _ in range(3)]

        for i in range(3):
            for j in range(3):
                button = Button(font_size=32)
                button.bind(on_press=self.make_move)
                self.grid_layout.add_widget(button)
                self.buttons[i][j] = button

        self.add_widget(self.grid_layout)
        self.current_player = 'X'
        
    def make_move(self, instance):
        if instance.text == '':
            instance.text = self.current_player
            if self.check_winner():
                self.status_label.text = f'Player {self.current_player} wins!'
                self.disable_buttons()
            elif self.check_draw():
                self.status_label.text = 'It\'s a draw!'
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'
                self.status_label.text = f'Player {self.current_player}\'s turn'
                if self.current_player == 'O':
                    self.ai_move()
        
    def ai_move(self):
        for i in range(3):
            for j in range(3):
                if self.buttons[i][j].text == '':
                    self.buttons[i][j].text = 'O'
                    if self.check_winner():
                        self.status_label.text = 'Player O wins!'
                        self.disable_buttons()
                        return
                    self.buttons[i][j].text = ''
        
        for i in range(3):
            for j in range(3):
                if self.buttons[i][j].text == '':
                    self.buttons[i][j].text = 'X'
                    if self.check_winner():
                        self.buttons[i][j].text = 'O'
                        self.current_player = 'X'
                        self.status_label.text = f'Player {self.current_player}\'s turn'
                        return
                    self.buttons[i][j].text = ''
        
        for i in range(3):
            for j in range(3):
                if self.buttons[i][j].text == '':
                    self.buttons[i][j].text = 'O'
                    self.current_player = 'X'
                    self.status_label.text = f'Player {self.current_player}\'s turn'
                    return
    
    def check_winner(self):
        for row in self.buttons:
            if row[0].text == row[1].text == row[2].text and row[0].text != '':
                return True
        for col in range(3):
            if self.buttons[0][col].text == self.buttons[1][col].text == self.buttons[2][col].text and self.buttons[0][col].text != '':
                return True
        if self.buttons[0][0].text == self.buttons[1][1].text == self.buttons[2][2].text and self.buttons[0][0].text != '':
            return True
        if self.buttons[0][2].text == self.buttons[1][1].text == self.buttons[2][0].text and self.buttons[0][2].text != '':
            return True
        return False
    
    def check_draw(self):
        for row in self.buttons:
            for button in row:
                if button.text == '':
                    return False
        return True
    
    def disable_buttons(self):
        for row in self.buttons:
            for button in row:
                button.disabled = True

class TicTacToeApp(App):
    def build(self):
        return TicTacToeGrid()

if __name__ == '__main__':
    TicTacToeApp().run()