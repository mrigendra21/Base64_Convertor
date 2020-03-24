# Base64_Convertor
Purpose of this script is to encode the Router's running config into Base64 format.

The flow to achieve this is pretty straight forward.

Step-1:
Open a file which contains the running config of any device and store the entire config into any variable.


Step-2:
Tranaslate the entire config into the binary format and make it a big binary string.


Step-3:
Now parse the binary string in such a way that it pick 6 bit of info in sequence and call the "returnCode" function to get the Base64 encoded value for that particular binary string.


Step-4:
Now merge the returned Base64 encoded value.
