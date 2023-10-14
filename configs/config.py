#Kafka Configuration
bootstrap_servers = "healthy-lionfish-5018-us1-kafka.upstash.io:9092"
sasl_mechanism = 'SCRAM-SHA-256'
security_protocol = 'SASL_SSL'
sasl_plain_username = 'aGVhbHRoeS1saW9uZmlzaC01MDE4JGxY2ft2THMMCzPDT8YMwZ08-V29NiXB6c8'
sasl_plain_password = 'MzU1OTg2NDgtMGY1Zi00ZDU4LTkzZGYtMjUwMzViNTcyZTIx'
sasl_jaas_config= "org.apache.kafka.common.security.scram.ScramLoginModule required username=\"aGVhbHRoeS1saW9uZmlzaC01MDE4JGxY2ft2THMMCzPDT8YMwZ08-V29NiXB6c8\" password=\"MzU1OTg2NDgtMGY1Zi00ZDU4LTkzZGYtMjUwMzViNTcyZTIx\";"
# wikimedia config
wikimedia_stream_url = "https://stream.wikimedia.org/v2/stream/recentchange"

