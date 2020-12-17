# inst326_group_project
1. Install the bs4 module
```
pip install bs4
```
2. If you are using an iOS device, go to spotlight and type ***Install Certificates.command***, then press Enter.

3. There are 3 classes each in files *number.py*, *tarot.py*, and *music.py*
   - ***number.py*** Deals with the translation of input digits/sentence.
     - *test_number.py* is the corresponding pytest.  
   - ***tarot.py*** Deals with opening a webpage that shows the picture of the tarot card drawn.
     - *test_tarot.py* is the corresponding pytest.  
   - ***music.py*** Deals with opening a webpage that relates to the tarot card picked by the user.
     - *test_music.py* is the corresponding pytest.  

4. Open ***main.py***, in the command line, input either of the two options:

   - Case 1:
    ```
    python3 main.py --number <Insert a four-digit letter (no need quotes)> 
    ```

   - Case 2: 
    ```
    python3 main.py --sentence <Insert a sentence you like>
    ```
5. 
- For case 1, the code should create one png file called ***your_color.png***. The file is a heart filled by your signature color. 
- For case 2, the code would create two png files called ***your_color.png*** and ***letter_frequency.png***. 
The first png file is the same as case 1, while the latter file is a histogram that represents the most common letter appeared in your input sentence.

6. Our code would also open a tab on your browser that shows you a picture of which tarot card you've drawn based on the 4-digit/sentence input. 

7. Our code should also open another tab on your browser that suggests you a k-pop song corresponding to your input 4-digit/sentence.

8. Lastly, in the terminal, you should see the name of your signature color and the meaning of the tarot card you've drawn.
