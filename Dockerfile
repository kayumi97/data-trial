FROM apache/airflow:slim-2.6.2

USER root
RUN apt-get update && apt-get install -y procps openjdk-11-jre gcc
USER airflow

ADD https://repo1.maven.org/maven2/org/apache/spark/spark-hadoop-cloud_2.12/3.4.1/spark-hadoop-cloud_2.12-3.4.1.jar /opt/airflow/jars/spark-hadoop-cloud_2.12-3.4.1.jar
ADD https://repo1.maven.org/maven2/org/apache/hadoop/hadoop-aws/3.3.4/hadoop-aws-3.3.4.jar /opt/airflow/jars/hadoop-aws-3.3.4.jar
ADD https://repo1.maven.org/maven2/org/apache/commons/commons-pool2/2.11.1/commons-pool2-2.11.1.jar /opt/airflow/jars/commons-pool2-2.11.1.jar
ADD https://repo1.maven.org/maven2/com/amazonaws/aws-java-sdk-bundle/1.12.262/aws-java-sdk-bundle-1.12.262.jar /opt/airflow/jars/aws-java-sdk-bundle-1.12.262.jar

USER root
RUN chmod a+r /opt/airflow/jars/spark-hadoop-cloud_2.12-3.4.1.jar \
    && chmod a+r /opt/airflow/jars/hadoop-aws-3.3.4.jar \
    && chmod a+r /opt/airflow/jars/commons-pool2-2.11.1.jar \
    && chmod a+r /opt/airflow/jars/aws-java-sdk-bundle-1.12.262.jar

RUN apt-get update && apt-get install -y iputils-ping


USER airflow

COPY requirements.txt .
RUN pip install --no-cache apache-airflow==2.6.2  -r requirements.txt
