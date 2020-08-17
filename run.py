#!/home/alexander/Programmierung/Python/web_dev_env/bin/python
from UdemyPicker import Udemy

Udemy = Udemy('n')
Differenz = len(Udemy.aktuelle_links)-len(Udemy.links)
print("Du hattest bereits %d dieser Kurse." %(Differenz))
print("Insgesamt werden heute %d Kurse ausprobiert." %(len(Udemy.links)))
Udemy.sign_up()