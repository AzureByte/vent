#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

import npyscreen

from vent.helpers.meta import Version
from vent.helpers.paths import PathDirs
from vent.menus.help import HelpForm
from vent.menus.logs import LogsForm
from vent.menus.main import MainForm
from vent.menus.services import ServicesForm
from vent.menus.tutorial_forms import TutorialAddingFilesForm
from vent.menus.tutorial_forms import TutorialAddingPluginsForm
from vent.menus.tutorial_forms import TutorialBackgroundForm
from vent.menus.tutorial_forms import TutorialBuildingCoresForm
from vent.menus.tutorial_forms import TutorialGettingSetupForm
from vent.menus.tutorial_forms import TutorialIntroForm
from vent.menus.tutorial_forms import TutorialSettingUpServicesForm
from vent.menus.tutorial_forms import TutorialStartingCoresForm
from vent.menus.tutorial_forms import TutorialTerminologyForm


class VentApp(npyscreen.NPSAppManaged):
    """ Main menu app for vent CLI """
    keypress_timeout_default = 10
    repo_value = {}
    paths = PathDirs()
    first_time = paths.ensure_file(paths.init_file)
    if first_time[0] == True and first_time[1] != "exists":
        npyscreen.NPSAppManaged.STARTING_FORM = "TUTORIALINTRO"
    else:
        npyscreen.NPSAppManaged.STARTING_FORM = "MAIN"

    def add_forms(self):
        """ Add in forms that will have dynamic data """
        self.addForm("SERVICES", ServicesForm, name="Services\t\t\t\t\t\t\t\tPress ^T to toggle main\t\t\t\t\t\tPress ^Q to quit", color="STANDOUT")
        self.addForm("LOGS", LogsForm, name="Logs\t\t\t\t\t\t\t\tPress ^T to toggle main\t\t\t\t\t\tPress ^Q to quit", color="STANDOUT")

    def remove_forms(self):
        """ Remove forms that will have dynamic data """
        self.removeForm("SERVICES")
        self.removeForm("LOGS")

    def onStart(self):
        """ Override onStart method for npyscreen """
        self.paths.host_config()
        version = Version()
        self.addForm("MAIN", MainForm, name="Vent "+version+"\t\t\t\t\tPress ^T to toggle help\t\t\t\t\t\tPress ^Q to quit", color="IMPORTANT")
        self.addForm("HELP", HelpForm, name="Help\t\t\t\t\t\t\t\tPress ^T to toggle previous\t\t\t\t\t\tPress ^Q to quit", color="DANGER")
        self.addForm("TUTORIALINTRO", TutorialIntroForm, name="Vent Tutorial"+"\t\t\t\t\t\tPress ^Q to quit", color="DANGER")
        self.addForm("TUTORIALBACKGROUND", TutorialBackgroundForm, name="About Vent"+"\t\t\t\t\t\tPress ^Q to quit", color="DANGER")
        self.addForm("TUTORIALTERMINOLOGY", TutorialTerminologyForm, name="About Vent"+"\t\t\t\t\t\tPress ^Q to quit", color="DANGER")
        self.addForm("TUTORIALGETTINGSETUP", TutorialGettingSetupForm, name="About Vent"+"\t\t\t\t\t\tPress ^Q to quit", color="DANGER")
        self.addForm("TUTORIALBUILDINGCORES", TutorialBuildingCoresForm, name="Working with Cores"+"\t\t\t\t\t\tPress ^Q to quit", color="DANGER")
        self.addForm("TUTORIALSTARTINGCORES", TutorialStartingCoresForm, name="Working with Cores"+"\t\t\t\t\t\tPress ^Q to quit", color="DANGER")
        self.addForm("TUTORIALADDINGPLUGINS", TutorialAddingPluginsForm, name="Working with Plugins"+"\t\t\t\t\t\tPress ^Q to quit", color="DANGER")
        self.addForm("TUTORIALADDINGFILES", TutorialAddingFilesForm, name="Files"+"\t\t\t\t\t\tPress ^Q to quit", color="DANGER")
        self.addForm("TUTORIALSETTINGUPSERVICES", TutorialSettingUpServicesForm, name="Services"+"\t\t\t\t\t\tPress ^Q to quit", color="DANGER")
        self.add_forms()

    def change_form(self, name):
        """ Changes the form (window) that is displayed """
        self.switchForm(name)
