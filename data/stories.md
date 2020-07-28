## chemin heureux
* mood_saluer
   - utter_saluer_1
* mood_super
   - utter_heureux_continuez

## chemin sans saluer
* request_question
   - utter_continuez

## chemin triste 1
* mood_saluer
   - utter_saluer_1
* mood_malheureux
   - utter_encouragent
   - utter_cela_a_t_il_aide
* mood_affirmer
   - utter_heureux_continuez

## chemin triste 2
* mood_saluer
   - utter_saluer_1
* mood_malheureux
   - utter_encouragent
   - utter_cela_a_t_il_aide
* mood_nier
   - utter_au_revoir

## dites au revoir
* mood_au_revoir
   - utter_au_revoir

## bot challenge_1
* mood_bot_challenge
   - utter_iamabot_1

## parcours_1
* mood_parcours
   - utter_parcours
   - parcours
   - utter_satisfaction
   
## formation_1
* mood_formation{"formation":"Parcours-Informatique"}
   - formation
   
## matiere_1
* mood_matiere{"matiereee":"xxx"}
   - matiere
   - slot{"msg":"helloword"}
