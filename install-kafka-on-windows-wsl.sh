wget https://archive.apache.org/dist/kafka/3.5.0/kafka-3.5.0-src.tgz
tar -xzf kafka-3.5.0-src.tgz

#Ensure that the kafka is installed
~/kafka_2.13-3.5.0/bin/kafka-topics.sh

#set the path in the .bashrc file
sudo echo PATH="$PATH:~/kafka_2.13-3.5.0/bin/">> .bashrc

#Now you should be able to run kafka binaries without using the entire path.
