# ChickenLanguageDataset
A dataset of chicken vocalizations intended to create machine learning models for chicken to human language translation and for a better understanding of poultry needs. There is a lot of nuance in chicken vocalizations that only an experienced poultry farmer can pick up on. Nicholas and Elsie Collias of the University of California, Los Angeles, catalogued more than 24 distinct chicken calls and their probable meanings, based on careful observation<sup>1</sup>.

This project was inspired by [Con Slobodchikoff](http://chasingdoctordolittle.com)'s incredible [work with prairie dogs](https://www.youtube.com/watch?v=y1kXCh496U0). 

## This dataset contains two types of data: 
1. Single vocalizations done by a single chicken, intended for translation
2. Longer segments of audio recorded that may include multiple chickens (for instance, data recorded in the coop of a poultry farm) that can provide a general sense of chicken well-being

## Current vocalizations studied:
1. Greeting. I believe this to be dependent on the person or animal being greeted, as chickens are thought to give distinct names to different people.
2.“I need to lay an egg and someone is in my nest box!”
3. "Give me some privacy - I'm laying an egg." (this is a prehistoric sounding screech)
4. “I laid an egg!” - sounds like "buck buck buck buh KACK!"
5. "Where is everybody" - I am unsure of whether this is the same call as their call after laying an egg or if there are subtle differences. I'd also like to study the nuance of these calls to see whether they are letting other chickens know where *they* are).
6. Ground predator warning - I would like to study these calls to see if their are different calls for different threats, similar to prairie dog communication
7. Aerial predator warning
8. Loud upset squawks - I would like to study whethere this call is different for hunger, thirst, heat or other malaise.
9. Noise mother hen makes to tell chicks to follow her
10. Tidbitting noise (hen to chicks) - sounds like "Cluck cluck"
11. Tidbitting noise (rooster to hen)
12. "Ouch" or "stop it" (squawking noise a chicken makes when pecked or startled)
13. Happy noises while eating
14. Happy noises while taking a dust bath
15. Unknown - unique vocalizations that I have not heard before.

## Contributions
I welcome contributions! 
Please submit data as a wav file to the respective folder for the type of call you believe it to be. If you are not sure of where they fit, please either submit to "unknown" folder or create a pull request to create a new folder. 

### File naming and metadata
Name your file precisely what you thought your chicken(s) was trying to say. If there are other files with the same name already in the dataset, give your recording name a unique numerical identifier.
Here are some examples of file names for each of the vocalization categories:

1. Greeting -  Name file after who chickens were greeting (e.g. primarycaretaker-.wav, stranger.wav, etc)
2. nest_box_needed.wav
3. privacy_please.wav
4. “I laid an egg!” - e.g. egg_song1.wav
5. "Where is everybody" - where_is_everybody.wav
6. Ground predator warning - e.g. golden_retreiver.wav OR golden_retriever_who_has_attacked_chickens_before.wav
7. Aerial predator warning - e.g. eagle.wav, crow.wav
8. Upset noises - i.e. hungry.wav, thirsty.wav, 90Fheat.wav
9. Noise mother hen makes to tell chicks to follow her - hen_telling_chicks_to_follow_her.wav
10. Tidbitting noise (hen to chicks) - tidbitting_hen.wav
11. Tidbitting noise (rooster to hen) - tidbitting_rooster.wav
12. ouch.wav
13. eating.wav
14. dust_bath.wav
15. Unknown - e.g. "chicken_looking_for_me_through_window.wav"

If possible, include metadata including time of day, weather, chicken breed, and any other relevant details (this is not required, so please don't let the extra time this takes be an obstacle to submitting data).
It's OK if there is background noise during the recording, as long as it's not someone's private conversation. 

Thanks so much! 

<sub>1. [Fowl Language: AI Decodes the Nuances of Chicken “Speech”](https://www.scientificamerican.com/article/fowl-language-ai-decodes-the-nuances-of-chicken-ldquo-speech-rdquo/)</sub>
