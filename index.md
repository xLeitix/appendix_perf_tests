# Online Appendix "An Exploratory Study of the State of Practice of Performance Testing in Java-Based Open Source Projects"

Here we collect some raw data and additional material to the paper _"An Exploratory Study of the State of Practice of Performance Testing in Java-Based Open Source Projects"_, by Philipp Leitner and Cor-Paul Bezemer.
Please access the data by cloning this repository:

`git clone https://github.com/xLeitix/appendix_perf_tests.git`

## Data Gathering and Analysis Scripts
All scripts used to collect the data and produce the metrics discussed in the paper (plus some that are not in the paper) are available in the directory `scripts`.
Data retrieval is done via Python 2.6 and using the BeautifulSoup library. Analysis is done in a combination of Python and R.

## Project Data Set and Coding Summary
The file `coding\project summary and statistics.xslx` contains all projects we considered, basic stats (number of stars, committers, ...), links to GitHub, and brief project summaries. Further, the file summarizes which observations we have made for each project, as well as a list of identified performance test files per project.

## Full Dataset
While all this data is also available in the Excel file, for convenience we also provide a table of all projects in our data set below. False positives are already excluded in this list (but they are contained in the Excel file).

| **Project Name** | **GitHub Link** | **Brief Description** |
| ---- | ---- | ---- | ---- |
| agraph-java-client	| https://github.com/franzinc/agraph-java-client.git	| Triple Store (Semantic Web) |
| AIF2 |	https://github.com/b0noI/AIF2.git | AIF2 - is fully language independent NLP library |
| arangodb-java-driver |	https://github.com/arangodb/arangodb-java-driver.git	| a Java driver for ArangoDB |
| async-google-pubsub-client | https://github.com/spotify/async-google-pubsub-client.git	| A performant Google Cloud Pub/Sub client and batch publisher |
| aviator | https://github.com/killme2008/aviator.git | Aviator is a lighweith,high performance expression evaluator for java |
| bigqueue | https://github.com/bulldog2011/bigqueue.git | A big, fast and persistent queue based on memory mapped file |
| BridJ |	https://github.com/nativelibs4java/BridJ.git | BridJ: blazing fast Java / C / C++ interop |
| Chronicle-Engine | https://github.com/OpenHFT/Chronicle-Engine.git | A high performance, low latency, reactive processing framework |
| Chronicle-Map |	https://github.com/OpenHFT/Chronicle-Map.git | Replicate your Key Value Store across your network, with consistency, persistance and performance |
| Chronicle-Queue |	https://github.com/OpenHFT/Chronicle-Queue.git | a distributed unbounded persisted queue |
| Chronicle-Wire |	https://github.com/OpenHFT/Chronicle-Wire.git	| Wire formatting in Chronicle |
| cloudhopper-smpp |	https://github.com/twitter/cloudhopper-smpp.git	|	Twitter's efficient, scalable, and flexible Java implementation of the Short Messaging Peer to Peer Protocol (SMPP) |
| Cojac |	https://github.com/Cojac/Cojac.git	|	Numerical Sniffer and Enriching Wrapper for Java |
| commons-beanutils |	https://github.com/apache/commons-beanutils.git	| an easy-to-use but flexible wrapper around reflection and introspection |
| commons-codec |	https://github.com/apache/commons-codec.git	| simple encoder and decoders for various formats such as Base64 and Hexadecimal |
| commons-csv |	https://github.com/apache/commons-csv.git	| a simple interface for reading and writing CSV files of various types |
| commons-jexl |	https://github.com/apache/commons-jexl.git	|	Implementation of JSTL Expression Language |
| commons-lang |	https://github.com/apache/commons-lang.git	|	utility class lib for Java	|
| commons-math |	https://github.com/apache/commons-math.git	|	math utilities |
| commons-ognl |	https://github.com/apache/commons-ognl.git	|	object graph navigation |
| commons-pool |	https://github.com/apache/commons-pool.git	|	object pooling |
| compress |	https://github.com/ning/compress.git	|	 Java LZF codec |
| concurrentlinkedhashmap	| https://github.com/ben-manes/concurrentlinkedhashmap.git	|	A high performance version of java.util.LinkedHashMap for use as a software cache |
| core | https://github.com/jetlang/core.git	|	Jetlang provides a high performance java threading library. The library is based upon Retlang |
| cyclops-react	| https://github.com/aol/cyclops-react.git	|	A comprehensive functional reactive platform for JDK8 |
| DeuceSTM |	https://github.com/DeuceSTM/DeuceSTM.git	|	Java Software Transactional Memory |
| DrizzleJDBC	| https://github.com/krummas/DrizzleJDBC.git	| 	JDBC driver for MySQL and Drizzle |
| druid |	https://github.com/alibaba/druid.git	|	Druid is the best database connection pool in JAVA |
| elasticsearch-lang-groovy |	https://github.com/elastic/elasticsearch-lang-groovy.git	|	Groovy lang Plugin for Elasticsearch |
| emfjson-jackson |	https://github.com/emfjson/emfjson-jackson.git	| JSON Binding for Eclipse Modeling Framework |
| Evictor |	https://github.com/stoyanr/Evictor.git	|	Java library providing a concurrent map that supports timed entry eviction |
| exp4j |	https://github.com/fasseg/exp4j.git	|	A tiny math exp evaluator |
| extdirectspring	| https://github.com/ralscha/extdirectspring.git	|	Implementation of the Ext Direct protocol with Java and Spring |
| fastjson |	https://github.com/alibaba/fastjson.git	|	A fast JSON parser/generator |
| fast-serialization |	https://github.com/RuedigerMoeller/fast-serialization.git	| fast java serialization drop in-replacement |
| fluent-http |	https://github.com/CodeStory/fluent-http.git	|	"This is the simplest fastest full fledged web server we could come up with." |
| fongo |	https://github.com/fakemongo/fongo.git	|	Fongo is an in-memory java implementation of MongoDB |
| g414-hash |	https://github.com/sunnygleason/g414-hash.git	|	Collection of useful 64-bit hash utilities including Bloom filter and HashFile (64-bit CDB clone) implementation |
| graphdb-benchmarks	| https://github.com/socialsensor/graphdb-benchmarks.git	| Graph DB benchmarks	|
| h2o-2 |	https://github.com/h2oai/h2o-2.git	| fast stats library	|
| HadoopUSC |	https://github.com/madiator/HadoopUSC.git	|	USC Version of Hadoop that includes HDFS-RAID. Erasure codes like Locally Repairable Codes (aka Simple Regenerating Code), Reed Solomon Code and XOR code are supported |
| hbase |	https://github.com/cloudera/hbase.git	| Apache Hbase |
| HBASE-SEARCH | https://github.com/jasonrutherglen/HBASE-SEARCH.git	| HBase with Lucene Search added |
| heftydb	| https://github.com/jordw/heftydb.git	| High performance persistent LSM key-value store library |
| hierarchical-clustering-java |	https://github.com/lbehnke/hierarchical-clustering-java.git	|	Implementation of an agglomerative hierarchical clustering algorithm |
| ifpress-solr-plugin | https://github.com/safarijv/ifpress-solr-plugin.git	| provides Solr plugins used at Safari |
| jackson-core |	https://github.com/FasterXML/jackson-core.git	| low-level incremental ("streaming") parser and generator abstractions |
| jackson-databind	| https://github.com/FasterXML/jackson-databind.git	| data-binding package for Jackson |
| jackson-dataformat-avro	| https://github.com/FasterXML/jackson-dataformat-avro.git	| Jackson dataformat module to support Avro-encoded data |
| jackson-dataformat-csv	| https://github.com/FasterXML/jackson-dataformat-csv.git	| Jackson data format module for reading and writing CSV encoded data |
| jackson-dataformat-smile |	https://github.com/FasterXML/jackson-dataformat-smile.git	| Jackson extension that adds support for Smile |
| jackson-dataformat-yaml	| https://github.com/FasterXML/jackson-dataformat-yaml.git	| Jackson module to add YAML backend (parser/generator adapters) |
| jackson-module-afterburner| https://github.com/FasterXML/jackson-module-afterburner.git	|	(depreciated) module of jackson for serialization |
| java-client	| https://github.com/appium/java-client.git	|	Java language binding for writing Appium Tests, conforms to Mobile JSON Wire Protocol |
| java-memcached-client	| https://github.com/dustin/java-memcached-client.git	| A simple, asynchronous, single-threaded memcached client |
| javassist |	https://github.com/jboss-javassist/javassist.git	| Java bytecode engineering |
| Java-Thread-Affinity | https://github.com/peter-lawrey/Java-Thread-Affinity.git	| Control thread affinity for Java |
| jcunit | https://github.com/dakusui/jcunit.git	| a framework to perform combinatorial tests using 'pairwise'(or more generally 't-wise') technique |
| JDBM3 | https://github.com/jankotek/JDBM3.git	|	provides TreeMap, HashMap and other collections backed up by disk storage |
| jeromq |	https://github.com/zeromq/jeromq.git	| Pure Java ZeroMQ |
| jnats | 	https://github.com/nats-io/jnats.git	| 	A Java client for NATS |
| jocket |	https://github.com/pcdv/jocket.git	| 	Low-latency socket implementation |
| joinery	| https://github.com/cardillo/joinery.git	|	 a data analysis library for joining together pieces of data to produce insight |
| jongo |	https://github.com/bguerout/jongo.git	|	Query in Java as in Mongo shell |
| Journal.IO |	https://github.com/sbtourist/Journal.IO.git	| Journal.IO is a lightweight, fast and easy-to-use journal storage implementation based on append-only rotating logs and checksummed variable-length records \
| jsword |	https://github.com/crosswire/jsword.git	|	Bible Study Software |
| kamikaze	| https://github.com/javasoze/kamikaze.git	|	DocId set compression and set operation library |
| KeptCollections	| https://github.com/anthonyu/KeptCollections.git	|	distributed Java collections for ZooKeeper |
| kontraktor |	https://github.com/RuedigerMoeller/kontraktor.git	|	high performance, lightweight and boilerplate free distributed eventloop'ish Actor implementation (specifically high-performance) |
| kumo |	https://github.com/kennycason/kumo.git	|	Word cloud API|
| lorsource	| https://github.com/maxcom/lorsource.git	|	?? |
| luxun |	https://github.com/bulldog2011/luxun.git	|	A high-throughput, persistent, distributed, publish-subscribe messaging system based on memory mapped file and Thrift RPC |
| matrix-toolkits-java |	https://github.com/fommil/matrix-toolkits-java.git	|	MTJ is a high-performance library for developing linear algebra applications |
| Metronome |	https://github.com/jpatanooga/Metronome.git	|	Metronome is a suite of parallel iterative algorithms that run natively on Hadoop's Next Generation YARN platform |
| nanojson |	https://github.com/mmastrac/nanojson.git	|	nanojson is a tiny, fast, and compliant JSON parser and writer for Java |
| nativetask |	https://github.com/decster/nativetask.git	|	Hadoop task level native runtime |
| neo4j-jdbc |	https://github.com/rickardoberg/neo4j-jdbc.git	| Neo4j JDBC driver for Neo4j 3.x with BOLT protocol |
| neo4j-reco |	https://github.com/graphaware/neo4j-reco.git	|	Neo4j Recommendation Engine |
| neo4j-relcount |	https://github.com/graphaware/neo4j-relcount.git	|	Neo4j relationship counter |
| nom-tam-fits |	https://github.com/nom-tam-fits/nom-tam-fits.git	|	Pure java Java library for reading and writing FITS files. FITS, the Flexible Image Transport System, is the format commonly used in the archiving and transport of astronomical data. |
| ognl |	https://github.com/jkuhnert/ognl.git	|	Object Graph Navigation Library |
| ordered-scheduler	| https://github.com/Ullink/ordered-scheduler.git	|	Unlock code that have sequence / ordering requirements |
| Orestes-Bloomfilter |	https://github.com/Baqend/Orestes-Bloomfilter.git	|	Library of different Bloom filters in Java with optional Redis-backing, counting and many hashing options |
| parsecj	| https://github.com/jon-hanson/parsecj.git	|	Java monadic parser combinator framework |
| passay |	https://github.com/vt-middleware/passay.git	| Password policy enforcement |
| prova |	https://github.com/prova/prova.git	| Prova is an economic and efficient, Java JVM based, open source rule language for reactive agents and event processing |
| pure-idea |	https://github.com/ikarienator/pure-idea.git	|	IntelliJ plugin for PureScript |
| rabbitmq-java-client |	https://github.com/rabbitmq/rabbitmq-java-client.git	| Java client lib for RabbitMQ |
| remoting |	https://github.com/jenkinsci/remoting.git	| Jenkins remoting is an executable JAR, which implements communication layer in Jenkins automation server |
| restheart	| https://github.com/SoftInstigate/restheart.git	|	Automatic REST API Server for MongoDB |
| rxjava-extras |	https://github.com/davidmoten/rxjava-extras.git	|	Utilities for use with rxjava |
| SAX |	https://github.com/jMotif/SAX.git	| Time series discretization with SAX |
| secor | 	https://github.com/pinterest/secor.git	|	Secor is a service persisting Kafka logs to Amazon S3, Google Cloud Storage and Openstack Swift (by Pinterest) |
| simpleel |	https://github.com/alibaba/simpleel.git	|	Simple Expression Language |
| simplehbase	| https://github.com/zhang-xzhi/simplehbase.git	|	Simplehbase is a lightweight ORM framework between java app and hbase |
| siren-join |	https://github.com/sirensolutions/siren-join.git	|	a plugin for Elasticsearch |
| SmartUnit	| https://github.com/rlogiacco/SmartUnit.git	|	"SmartUnit is intended to be a place where unit test utility and helper classes can be collected to be shared." |
| snaptree |	https://github.com/nbronson/snaptree.git	| concurrent AVL tree |
| spark-solr	| https://github.com/lucidworks/spark-solr.git	| includes tools for reading data from Solr as a Spark RDD and indexing objects from Spark into Solr using SolrJ |
| spatial |	https://github.com/neo4j-contrib/spatial.git	|	Neo4j Spatial is a library of utilities for Neo4j that faciliates the enabling of spatial operations on data |
| spatialhadoop |	https://github.com/aseldawy/spatialhadoop.git	| ?? |
| st9-proto-service	| https://github.com/sunnygleason/st9-proto-service.git	| A RESTful Content Store designed with scalability in mind |
| tablesaw	| https://github.com/lwhite1/tablesaw.git	| Part data frame. Part column store. All Java. |
| tachyon-perf |	https://github.com/PasaLab/tachyon-perf.git	| A general performance test framework for Tachyon |
| tr13 |	https://github.com/ning/tr13.git	| a library for constructing and using read-only compact (memory-efficient) in-memory trie data structures |
| transmittable-thread-local |	https://github.com/alibaba/transmittable-thread-local.git	| A simple 0-dependency java lib for transmitting ThreadLocal value between threads even using thread pool |
| Trident |	https://github.com/TridentSDK/Trident.git	| Minecraft server |
| tyrant |	https://github.com/mikera/tyrant.git	|	Tyrant Roguelike game in Java |
| UncleJim |	https://github.com/GlenKPeterson/UncleJim.git	| A library for the practical application of Functional Programming |
| urlrewritefilter |	https://github.com/paultuckey/urlrewritefilter.git	| A Java Web Filter with functionality like Apache's mod_rewrite |
| vectorz	| https://github.com/mikera/vectorz.git	| Fast and flexible numerical library for Java featuring N-dimensional arrays |
| vibur-dbcp |	https://github.com/vibur/vibur-dbcp.git	| concurrent and dynamic JDBC connection pool |
| vibur-object-pool |	https://github.com/vibur/vibur-object-pool.git	| a general-purpose concurrent Java object pool |
| webx-restful |	https://github.com/alibaba/webx-restful.git	| citrus-rpc |
