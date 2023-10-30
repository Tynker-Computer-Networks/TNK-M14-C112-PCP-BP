Build the GUI
===================
​
In this activity, you will create a GUI for the Quiz app and accept an answer from the input box.
​
​

<img src= "https://s3-whjr-curriculum-uploads.whjr.online/7e69df3a-1296-449b-ab11-01875a0f84d6.gif" width = "521" height = "281" >

Follow the given steps to complete this activity:
​
​* Open file `client.py`.
​
* Create a Scrollbar widget and assigns it to the variable scrollbar to associate with the self.text_comm text widget.
```sh
scrollbar = Scrollbar(self.text_comm)
```

* Place scrollbar on right side and give it size accordingly.
```
scrollbar.place(relheight = 1, relx = 0.974)
```

* Configure the scrollbar to control the vertical (y-axis) scrolling of the associated text widget.
```sh
scrollbar.config(command = self.text_comm.yview)
```

* Configure the state of the self.text_comm text widget to "NORMAL." in the show_message() method.
```sh
self.text_comm.config(state = NORMAL)
```     

* Use insert method on text_comm to add the message to the self.text_comm text widget, and pass END argument to add message at the end of the widget and the +"\n\n" to append two newline characters to create a gap between the current content and the new message.
```sh
self.text_comm.insert(END, message+"\n\n")
``` 
   
* Configure text_comm state to DISABLED for locking the widget, making it uneditable by the user.
```sh
self.text_comm.config(state = DISABLED):
``` 
   
* Use see(END) method to scroll to end of the text_comm.
```sh
self.text_comm.see(END)
``` 
   
* Save and run the code to check the output.