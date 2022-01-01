from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.properties import NumericProperty

class xToDoubt(App):

	def load(self):
		with open('doubt.txt') as fobj:
			for count in fobj:
				self.doubt = int(count.rstrip())

	def save(self):
		with open('doubt.txt', 'w') as fobj:
			fobj.write(str(self.doubt))

	def build(self):

		h_layout = BoxLayout(size_hint=(1, .85))
		header_layout = BoxLayout(size_hint=(1, .15))
		main_layout = BoxLayout(orientation="vertical")

		doubt=self.load()

		self.header = Label(
					text='Level of Doubt: \n' + str(f'{self.doubt:,}'),
					pos_hint={"center_x": 0, "center_y": .5},
					size_hint=(.7, 1),
                    font_size=26,
                    bold=True
			)

		xButton = Button(
                    text='[X]',
                    pos_hint={"center_x": 0.5, "center_y": 0.5},
                    background_color="blue",
                    background_normal='',
                    color='white',
                    font_size=80,
                    bold=True
                    )
		resetButton = Button(
					text='Reset',
					background_color='red',
					size_hint=(.3, 1),
					pos_hint={"center_x": 0.5, "center_y": 0.5},
					bold=True
					)

		xButton.bind(on_press=self.doubtCounter)
		resetButton.bind(on_press=self.resetCounter)

		header_layout.add_widget(self.header)
		header_layout.add_widget(resetButton)
		main_layout.add_widget(header_layout)

		main_layout.add_widget(xButton)

		return main_layout

	def doubtCounter(self, widget):
		self.doubt+=1
		self.save()
		self.header.text='Level of Doubt: \n' + str(f'{self.doubt:,}')

	def resetCounter(self, widget):
		self.doubt=0
		self.save()
		self.load()
		self.header.text='Level of Doubt: \n' + str(f'{self.doubt:,}')

if __name__ == "__main__":
    app = xToDoubt()
    app.run()
