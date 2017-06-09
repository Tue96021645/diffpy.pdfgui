#!/usr/bin/env python
# -*- coding: UTF-8 -*-
##############################################################################
#
# PDFgui            by DANSE Diffraction group
#                   Simon J. L. Billinge
#                   (c) 2006 trustees of the Michigan State University.
#                   All rights reserved.
#
# File coded by:    Chris Farrow
#
# See AUTHORS.txt for a list of people who contributed.
# See LICENSE.txt for license information.
#
##############################################################################

# generated by wxGlade 0.4.1 on Wed Mar 29 13:54:14 2006

import os.path
import wx
from diffpy.pdfgui.gui.pdfpanel import PDFPanel

class JournalPanel(wx.Panel, PDFPanel):
    def __init__(self, *args, **kwds):
        PDFPanel.__init__(self)
        # begin wxGlade: JournalPanel.__init__
        kwds["style"] = wx.TAB_TRAVERSAL
        wx.Panel.__init__(self, *args, **kwds)
        self.textCtrlJournal = wx.TextCtrl(self, -1, "", style=wx.TE_MULTILINE)
        self.exportButton = wx.Button(self, -1, "Export")
        self.closeButton = wx.Button(self, wx.ID_CLOSE, "")

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_TEXT, self.onText, self.textCtrlJournal)
        self.Bind(wx.EVT_BUTTON, self.onExport, self.exportButton)
        self.Bind(wx.EVT_BUTTON, self.onClose, id=wx.ID_CLOSE)
        # end wxGlade
        self.__customProperties()

    def __set_properties(self):
        # begin wxGlade: JournalPanel.__set_properties
        pass
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: JournalPanel.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_2 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_1.Add(self.textCtrlJournal, 1, wx.EXPAND, 0)
        sizer_2.Add((1, 1), 1, 0, 0)
        sizer_2.Add(self.exportButton, 0, wx.ALL, 5)
        sizer_2.Add(self.closeButton, 0, wx.ALL, 5)
        sizer_1.Add(sizer_2, 0, wx.EXPAND, 0)
        self.SetSizer(sizer_1)
        sizer_1.Fit(self)
        # end wxGlade

    def __customProperties(self):
        """Custom Properties go here."""
        self.fullpath = ""

        # Bind the focus loss of the text control
        self.textCtrlJournal.Bind(wx.EVT_KEY_DOWN, self.onKey)
        return

    def onText(self, event): # wxGlade: JournalPanel.<event_handler>
        """Record anything that is written into the journal."""
        text = self.textCtrlJournal.GetValue()
        if text != self.mainFrame.control.journal:
            self.mainFrame.control.journal = text
            self.mainFrame.needsSave()
        return

    def onExport(self, event): # wxGlade: JournalPanel.<event_handler>
        """Export the journal to an external file."""
        matchstring = "Text files (*.txt)|*.txt|All Files|*"
        dir, filename = os.path.split(self.fullpath)
        if not dir: dir = self.mainFrame.workpath
        d = wx.FileDialog(None, "Export to...",
                dir, filename, matchstring,
                wx.SAVE|wx.OVERWRITE_PROMPT)

        if d.ShowModal() == wx.ID_OK:
            self.fullpath = d.GetPath()
            self.mainFrame.workpath = os.path.dirname(self.fullpath)
            outfile = open(self.fullpath, 'w')
            outfile.write(self.mainFrame.control.journal)
            outfile.close()
        d.Destroy()
        return

    def onClose(self, event): # wxGlade: JournalPanel.<event_handler>
        self._close()
        return

    def _close(self):
        self.mainFrame.onShowJournal(None)
        return

    def onKey(self, event):
        """Catch Ctrl+J to close the journal."""
        # Ctrl J
        key = event.GetKeyCode()
        if event.ControlDown() and key == 74:
            self._close()
        event.Skip()
        return

    # Methods overloaded from PDFPanel
    def refresh(self):
        """Fill the jounalTextCtrl with the journal."""
        # This will make sure that the scroll position does not change.
        text = self.textCtrlJournal.GetValue()
        if text != self.mainFrame.control.journal:
            self.textCtrlJournal.ChangeValue(self.mainFrame.control.journal)
            self.textCtrlJournal.SetInsertionPointEnd()
        pos = self.textCtrlJournal.GetInsertionPoint()
        self.textCtrlJournal.ShowPosition(pos)
        return


# end of class JournalPanel