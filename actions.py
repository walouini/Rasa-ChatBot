# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

import pymongo
from pymongo.database import Database
from pymongo import MongoClient


class ActionHelloWorld(Action):

     def name(self) -> Text:
         return "action_hello_world"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

         dispatcher.utter_message(text="Helloooo World =) :D !!!")

         return []


class matiere(Action):
    def name(self) -> Text:
        return "matiere"
    
    def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        #connect to mongodb
        connection = pymongo.MongoClient("localhost", 27017)
        #attach to admin db
        db = connection["admin"]
        #get handle for client collection
        res = db["parcours_informatique"]
        #get slot
        facility = tracker.get_slot("matiereee")
        #find a single document
        item = res.find({"nom":"facility"})
        for i in item:
            msg = (i["nom"] + ":\n" + "- parcours " +i["parcours"] + "\n" + "- " + i["semestre"] + "\n" + "- UE " + i["UE"] + "\n" + "- heures_denseignement " + i["heures_denseignement"] + "\n" + "- credits " + i["credits"] + "\n")
        msg = "helloword"
        dispatcher.utter_message("msg test de : {} : {}".format(facility, msg))    
        return [SlotSet("msg",msg)]
    
    
class parcours(Action):
    def name(self):
        return "parcours"
    
    def run(self, dispatcher, tracker, domain):
        #connect to mongodb
        connection = pymongo.MongoClient("localhost", 27017)
        #attach to admin db
        db = connection["admin"]
        #get handle for client collection
        res = db["parcours"]
        #find a single document
        item = res.find({"parcours":"informatique"})
        #dispatcher.utter_message("{} : \n".format(parcourrr))
        for i in item:
            dispatcher.utter_message(i["nom"] + " :  \n" + "- " + i["description"] + "\n")
            #dispatcher.utter_message("\n")
        return []
    
class formation(Action):
    def name(self):
        return "formation"
    
    def run(self, dispatcher, tracker, domain):
        #connect to mongodb
        connection = pymongo.MongoClient("localhost", 27017)
        #attach to admin db
        db = connection["admin"]
        #get slot
        facility = tracker.get_slot("parcour")
        #get handle for client collection
        res = db["parcours_informatique"]
        #find a single document
        item = res.find({"semestre":"semestre 1"})
        dispatcher.utter_message("semestre 1 :  \n")
        for i in item:
            dispatcher.utter_message("- " + i["nom"] + "  //  UE: " + i["UE"] + " //  heures_denseignement: " + i["heures_denseignement"] + "  // credits: " + i["credits"] + " //  \n")
        item = res.find({"semestre":"semestre 2"})
        dispatcher.utter_message("semestre 2 :  \n")
        for i in item:
            dispatcher.utter_message("- " + i["nom"] + "  //  UE: " + i["UE"] + " //  heures_denseignement: " + i["heures_denseignement"] + "  // credits: " + i["credits"] + " //  \n")    
        item = res.find({"semestre":"semestre 3"})
        dispatcher.utter_message("semestre 3 :  \n")
        for i in item:
            dispatcher.utter_message("- " + i["nom"] + "  //  UE: " + i["UE"] + " //  heures_denseignement: " + i["heures_denseignement"] + "  // credits: " + i["credits"] + " //  \n")
        item = res.find({"semestre":"semestre 4"})
        dispatcher.utter_message("semestre 4 :  \n")
        for i in item:
            dispatcher.utter_message("- " + i["nom"] + "  //  UE: " + i["UE"] + " //  heures_denseignement: " + i["heures_denseignement"] + "  // credits: " + i["credits"] + " //  \n")
        item = res.find({"semestre":"semestre 5"})
        dispatcher.utter_message("semestre 5 :  \n")
        for i in item:
            dispatcher.utter_message("- " + i["nom"] + "  //  UE: " + i["UE"] + " //  heures_denseignement: " + i["heures_denseignement"] + "  // credits: " + i["credits"] + " //  \n")
        item = res.find({"semestre":"semestre 6"})
        dispatcher.utter_message("semestre 6 :  \n")
        for i in item:
            dispatcher.utter_message("- " + i["nom"] + "  //  UE: " + i["UE"] + " //  heures_denseignement: " + i["heures_denseignement"] + "  // credits: " + i["credits"] + " //  \n")    
        return []

    

