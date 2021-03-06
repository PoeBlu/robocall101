###### ROBOCALL101


<b>about</b><br><br>
This program posts a temporary XML/TWIML file to
<a href="https://www.restwords.com">restwords.com</a><br> to use as
a webhook. Then the Twilio API connects to that webhook<br>to make
a robocall on-the-fly. The Twilio bot will transcribe and<br>speak
exactly what you pass with the <code>-c</code> option
(including swears,<br>most slang, and large numbers).

A text may also be sent with the <code>-t</code> option.

Arnold is having a bad day - Use the <code>-a</code> option.<br>
(for extreme circumstances only)
<br><br>
<b>Requirements</b><br>
<ul>
  <li>Python3 and <code>pip install twilio</code></li>
  <li>Obtain your Twilio Credentials and Twilio Number</li>
  <li>Set the following environment variables:</li>
    <ol>
      <li>TWILIO_NUMBER=18885551234</li>
      <li>TWILIO_ACCOUNT_SID=XXXXXXXXXXXXXXXXXXXXXXXXXXXXX</li>
      <li>TWILIO_AUTH_TOKEN=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX</li>
    </ol>
</ul>

Twilio is free to try, but I recommend getting a paid number for $1 a month.
<br><br><br>
<b>example usage:</b><br>
<ul>
  <li>./robocall101.py -n 18881234567 -t "hello world"</li>
  <li>./robocall101.py -n 18881234567 -c "hello world"</li>
  <li>./robocall101.py -n 18881234567 -a</li>
</ul>

<pre>
  <code>
REQUIRED:
-n &lt;outgoing number&gt; 

PICK ONE:
-c/--call &lt;text/string here&gt; (Robocall on thy fly)
-t/--text &lt;text/string here&gt; (Send an SMS text message)
-a/--arnold (Call with Arnold recording)
  </code>
</pre>
<br>
<b>optionally install from git:</b><br>
<br><br>
<code>pip install git+https://github.com/rootVIII/robocall101</code><br>
(or pip3 depending on your setup)
<br><br>
This was developed on Ubuntu 18.04.4 LTS.
<hr>
<b>Author: rootVIII 09NOV2019</b><br><br>


  
