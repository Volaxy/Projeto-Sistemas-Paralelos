#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 7.2
#  in conjunction with Tcl version 8.6
#    Nov 02, 2022 07:32:04 PM -03  platform: Windows NT

import tkinter as tk

import cadastro

def main(*args):
    '''Main entry point for the application.'''
    global root
    root = tk.Tk()
    root.protocol( 'WM_DELETE_WINDOW' , root.destroy)
    # Creates a toplevel widget.
    global _top1, _w1
    _top1 = root
    _w1 = cadastro.Toplevel1(_top1)
    root.mainloop()

if __name__ == '__main__':
    cadastro.start_up()



