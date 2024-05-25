from GUI_Master import RootGUI, CommGUI

RootMaster = RootGUI()
CommMaster = CommGUI(RootMaster.root)

RootMaster.root.mainloop()
