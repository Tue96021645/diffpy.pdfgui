#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-
# generated by wxGlade 0.6 on Mon Oct 15 14:14:18 2007

import wx
from diffpy.pdfgui.control.controlerrors import *
from wxExtensions.validators import TextValidator, FLOAT_ONLY
from pdfpanel import PDFPanel

# begin wxGlade: extracode
# end wxGlade

class BondLengthDialog(wx.Dialog):
    def __init__(self, *args, **kwds):
        # begin wxGlade: BondLengthDialog.__init__
        kwds["style"] = wx.DEFAULT_DIALOG_STYLE
        wx.Dialog.__init__(self, *args, **kwds)
        self.sizer_2_staticbox = wx.StaticBox(self, -1, "")
        self.instructionsLabel = wx.StaticText(self, -1, "Enter the indices of two atoms.")
        self.indicesLabel = wx.StaticText(self, -1, "Atom Indices")
        self.aSpinCtrl = wx.SpinCtrl(self, -1, "", min=0, max=100)
        self.bSpinCtrl = wx.SpinCtrl(self, -1, "", min=0, max=100)
        self.static_line_2 = wx.StaticLine(self, -1)
        self.instructionsLabel2 = wx.StaticText(self, -1, "Or enter the elemental symbols of two atoms and\nthe range over which to calculate the bond lengths.")
        self.elementLabel = wx.StaticText(self, -1, "Elements")
        self.aComboBox = wx.ComboBox(self, -1, choices=[], style=wx.CB_DROPDOWN)
        self.bComboBox = wx.ComboBox(self, -1, choices=[], style=wx.CB_DROPDOWN)
        self.rangeLabel = wx.StaticText(self, -1, "Range")
        self.lbTextCtrl = wx.TextCtrl(self, -1, "")
        self.toLabel = wx.StaticText(self, -1, "to")
        self.ubTextCtrl = wx.TextCtrl(self, -1, "")
        self.static_line_1 = wx.StaticLine(self, -1)
        self.cancelButton = wx.Button(self, wx.ID_CANCEL, "Cancel")
        self.okButton = wx.Button(self, wx.ID_OK, "OK")

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_SPINCTRL, self.onSpin, self.aSpinCtrl)
        self.Bind(wx.EVT_SPINCTRL, self.onSpin, self.bSpinCtrl)
        self.Bind(wx.EVT_BUTTON, self.onCancel, id=wx.ID_CANCEL)
        self.Bind(wx.EVT_BUTTON, self.onOk, id=wx.ID_OK)
        # end wxGlade
        self.__customProperties()

    def __set_properties(self):
        # begin wxGlade: BondLengthDialog.__set_properties
        self.SetTitle("Calculate Bond Lengths")
        self.aSpinCtrl.SetMinSize((80, 27))
        self.bSpinCtrl.SetMinSize((80, 27))
        self.aComboBox.SetMinSize((80, 27))
        self.bComboBox.SetMinSize((80, 27))
        self.lbTextCtrl.SetMinSize((80, 27))
        self.ubTextCtrl.SetMinSize((80, 27))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: BondLengthDialog.__do_layout
        sizer_2 = wx.StaticBoxSizer(self.sizer_2_staticbox, wx.VERTICAL)
        sizer_4_copy = wx.BoxSizer(wx.HORIZONTAL)
        sizer_4_copy_1 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_4 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_3 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_2.Add(self.instructionsLabel, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5)
        sizer_3.Add(self.indicesLabel, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5)
        sizer_3.Add(self.aSpinCtrl, 0, wx.ALL, 5)
        sizer_3.Add(self.bSpinCtrl, 0, wx.ALL, 5)
        sizer_2.Add(sizer_3, 0, wx.EXPAND, 0)
        sizer_2.Add(self.static_line_2, 0, wx.BOTTOM|wx.EXPAND, 5)
        sizer_2.Add(self.instructionsLabel2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5)
        sizer_4.Add(self.elementLabel, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5)
        sizer_4.Add(self.aComboBox, 0, wx.ALL, 5)
        sizer_4.Add(self.bComboBox, 0, wx.ALL, 5)
        sizer_2.Add(sizer_4, 0, wx.EXPAND, 0)
        sizer_4_copy_1.Add(self.rangeLabel, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5)
        sizer_4_copy_1.Add(self.lbTextCtrl, 0, wx.ALL, 5)
        sizer_4_copy_1.Add(self.toLabel, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5)
        sizer_4_copy_1.Add(self.ubTextCtrl, 0, wx.ALL, 5)
        sizer_2.Add(sizer_4_copy_1, 0, wx.EXPAND, 0)
        sizer_2.Add(self.static_line_1, 0, wx.EXPAND, 0)
        sizer_4_copy.Add((0, 0), 1, wx.EXPAND, 0)
        sizer_4_copy.Add(self.cancelButton, 0, wx.ALL, 5)
        sizer_4_copy.Add(self.okButton, 0, wx.ALL, 5)
        sizer_2.Add(sizer_4_copy, 0, wx.EXPAND, 0)
        self.SetSizer(sizer_2)
        sizer_2.Fit(self)
        self.Layout()
        # end wxGlade

    def __customProperties(self):
        """Set the custom properties."""
        self.a = 1
        self.b = 2
        self.ea = "ALL"
        self.eb = "ALL"
        self.lb = 0.1
        self.ub = 0.1

        # Set the textCtrl validators and focus events
        textCtrls = [self.lbTextCtrl, self.ubTextCtrl]
        for ctrl in textCtrls:
            ctrl.SetValidator(TextValidator(FLOAT_ONLY))
            ctrl.Bind(wx.EVT_KILL_FOCUS, self.onTextKillFocus) 

        self.comboBoxes = [self.aComboBox, self.bComboBox]
        for cbox in self.comboBoxes:
            cbox.Bind(wx.EVT_KILL_FOCUS, self.onComboKillFocus) 
        return

    def setStructure(self, structure):
        """Set the structure and update the widgets.

        This must be called before the spin control boxes will be settable to
        anything other than 1.
        """
        self.okButton.Enable(True)

        natoms = len(structure)
        if natoms < 2:
            self.okButton.Enable(False)
            return

        # Fill the spin controls
        self.aSpinCtrl.SetRange(1, natoms)
        self.bSpinCtrl.SetRange(1, natoms)
        self.aSpinCtrl.SetValue(min(1,natoms))
        self.bSpinCtrl.SetValue(min(2,natoms))

        # Fill the combo boxes
        eDict = dict.fromkeys([a.element for a in structure])
        self.eList = eDict.keys()
        self.eList.sort()
        self.eList.insert(0, "All")
        import string
        map(string.capitalize, self.eList)

        self.aComboBox.Clear()
        self.bComboBox.Clear()
        for el in self.eList:
            self.aComboBox.Append(el)
            self.bComboBox.Append(el)
        self.aComboBox.SetValue("All")
        self.bComboBox.SetValue("All")

        self.lbTextCtrl.SetValue("0.1")
        self.ubTextCtrl.SetValue("0.1")
        return

    def onTextKillFocus(self, event):
        self.lb = float(self.lbTextCtrl.GetValue())
        self.ub = float(self.ubTextCtrl.GetValue())

        if self.lb < 0.1: 
            self.lb = 0.1
            val = min(0.1, self.ub)
            self.lbTextCtrl.SetValue("%s"%val)
        if self.ub < 0.1: 
            self.ub = 0.1
            val = max(0.1, self.lb)
            self.ubTextCtrl.SetValue("%s"%val)
        return

    def onComboKillFocus(self, event):

        # Verify that the combo boxes are valid
        for cbox in self.comboBoxes:
            val = cbox.GetValue()
            if val not in self.eList:
                val = "All"
            cbox.SetValue(val)

        self.ea = self.aComboBox.GetValue()
        self.eb = self.bComboBox.GetValue()
        return

    def getCtrlLetter(self, ctrl):
        """Get the letter associated with the control."""
        if ctrl is self.aSpinCtrl: return "a"
        return "b"

    def onSpin(self, event): # wxGlade: BondLengthDialog.<event_handler>
        letters = ["a", "b"]
        ctrl = event.GetEventObject()
        val = event.GetSelection()

        atomLetter = self.getCtrlLetter(ctrl)

        # Check to see if the value is increasing or decreasing
        increasing = True
        oldval = getattr(self, atomLetter)
        if val < oldval: increasing = False

        # Check to see if the value is equal to another. If so, move it along in
        # the direction it was going.
        letters.remove(atomLetter)
        newval = val
        loop = True
        while loop:
            loop = False
            for l in letters:
                if newval == getattr(self, l):
                    loop = True
                    if increasing:
                        newval += 1
                    else:
                        newval -= 1

        # Set the new value, depending on what it is.
        if newval > 0 and newval <= ctrl.GetMax():
            setattr(self, atomLetter, newval)
            wx.CallAfter(ctrl.SetValue, newval)
        else:
            setattr(self, atomLetter, oldval)
            wx.CallAfter(ctrl.SetValue, oldval)
        return

    def onCancel(self, event): # wxGlade: BondLengthDialog.<event_handler>
        event.Skip()

    def onOk(self, event): # wxGlade: BondLengthDialog.<event_handler>
        event.Skip()


# end of class BondLengthDialog


if __name__ == "__main__":
    app = wx.PySimpleApp(0)
    wx.InitAllImageHandlers()
    blenDialog = BondLengthDialog(None, -1, "")
    app.SetTopWindow(blenDialog)
    blenDialog.Show()
    app.MainLoop()
