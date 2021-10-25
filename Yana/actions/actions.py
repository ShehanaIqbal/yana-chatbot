# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from database import database as db


class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Hello World!")

        return []


class QueryArticles(Action):

    def name(self) -> Text:
        return "action_find_articles"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        mood = tracker.get_slot("mood")
        if mood == 'නරක' or mood == 'හොද':
            dispatcher.utter_message(text='ඔබට ප්‍රයෝජනවත් වනු ඇතැයි මම සොයා ගත් ලිපි කිහිපයක් පහත දැක්වේ.')

            connection = db.create_connection()
            get_query_results = db.select_article_by_mood(connection, mood)
            print (get_query_results)
            count = 0
            for r in get_query_results:
                count += 1
                t = 'Article No : ' + str(count) + '\n' + 'Article name : ' + r[0] + '\n' + 'URL : ' + r[1]
                print(t)
                dispatcher.utter_message(text=t)

            return []
        else:
            dispatcher.utter_message(text='සමාවෙන්න, මට මීට පිලිතුරු දීමට අපහසුයි. මම තවම පුහුනු වන ගමන්.')
            return []


class QueryTherapists(Action):

    def name(self) -> Text:
        return "action_find_therapists"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="පහත දැක්වෙන්නේ ඔබට ප්‍රයෝජනවත් වනු ඇතැයි මම සොයා ගත් සම්බන්ධතා කිහිපයකි")
        connection = db.create_connection()
        # db.create_tables(connection)
        get_query_results = db.select_all_therapists(connection)
        count = 0
        for r in get_query_results:
            count += 1
            # 1. name, 2. description, 3. title, 4. contactNo, 5.area
            t = 'Therapist No : ' + str(count) + '\n' + 'Therapist Name : ' + r[0] + 'Title : ' + r[2] + 'Description : ' + \
                r[1] + '\n' + 'Contact No : ' + r[3] + '\n' + 'Area : ' + r[4]
            print(t)
            dispatcher.utter_message(text=t)

        return []

# class ActionSetUsername(Action):

#     def name(self) -> Text:
#         return "action_set_username"

#     def run(self, dispatcher, CollectingDispatcher,
#     tracker: Tracker,
#     domain: Dict[Text, Any])-> List[Dict[Text,any]]:
#         text = tracker.latest_message['text']
#         dispatcher.utter_message(text=f"{text}, එය ලස්සන නමක්.")
#         return [SlotSet("username",text)]

# class ActionGetUsername(Action):

#     def name(self) -> Text:
#         return "action_get_username"

#     def run(self, dispatcher, CollectingDispatcher,
#         tracker: Tracker,
#         domain: Dict[Text, Any])-> List[Dict[Text,any]]:

#         username = tracker.get_slot("username")
#         if not username:
#             return[""]
#         else:
#             return [username]
