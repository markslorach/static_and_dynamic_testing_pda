### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:


  def check_for_ace(self, card):
	# line below should be == instead of =
    if card.value = 1:
      return True
	# line below should have : after else
    else
      return False
   
	# line below should have a comma , between card1 and card 2	
  dif highest_card(self, card1 card2):
  if card1.value > card2.value:
	# line below should return card1 instead of card 
    return card
  else:
    return card2
  


def cards_total(self, cards):
	# in the line below total should = 0
  total
  for card in cards:
    total += card.value
	# the return in the line below shoud be place outside of the loop
    return "You have a total of" + total
  
```
