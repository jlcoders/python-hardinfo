#!/usr/bin/python3

import os
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class MyWindow(Gtk.Window):
   def __init__(self):
     Gtk.Window.__init__(self, title="Hardware Information", resizable=1)
     self.set_border_width(10)
     self.set_default_size(400,300)
     self.grid = Gtk.Grid()
     self.add(self.grid)

     self.label = Gtk.Label()
     self.label.set_yalign(0)
     self.label.set_xalign(0)
     self.grid.add(self.label)
     self.grid.attach(self.label, 1,1,1,1)

     ## botão atualizar
  
     self.button = Gtk.Button(label="Atualizar", margin_top=12, margin_bottom=19, margin_left=20)
     self.button.connect("clicked", self.atualizar)
     self.grid.add(self.button)

     self.temperatura = os.system("sensors | grep Core > temp_c")
     self.file = open("temp_c", "r")
     self.l = self.file.read()
     self.label.set_markup("<b>Temperatura:</b> \n{}".format(self.l))
     
     self.label2 = Gtk.Label()
     self.label2.set_markup("<b>RAM:</b>\n")
     self.grid.attach(self.label2, -0, 10, 1, 1)
     self.label2.set_yalign(40)
     self.label2.set_xalign(-20)
     
     self.memoria = os.system("free -h | grep Mem > memoria")
     self.file2 = open("memoria", "r")
     self.ler = self.file2.read()
     self.label2.set_markup("<b>RAM:</b>\n{}".format(self.ler))

   def atualizar(self, widget):
     self.temperatura = os.system("sensors | grep Core > temp_c")
     self.file = open("temp_c", "r")
     self.l = self.file.read()
     self.label.set_markup("<b>Temperatura:</b> \n{}".format(self.l))

win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()

