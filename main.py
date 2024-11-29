from kivymd.app import MDApp
from kivymd.uix.label import MDLabel

import scripts.database


class GymApp(MDApp):
    def build(self):
        # Create database
        scripts.database.database_connection()
        scripts.database.create_user_table()
        
        return MDLabel(text="Hello, KivyMD!", halign="center")

if __name__ == "__main__":
    GymApp().run()