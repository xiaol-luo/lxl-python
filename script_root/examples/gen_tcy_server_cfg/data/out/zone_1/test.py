# zone Zone
# server GameServer

<?xml version="1.0" encoding="UTF-8"?>
<root>
	<zone>zone_1</zone>
	<server_role>world</server_role>
	<server_name>zone_1_world_0</server_name>

	<etcd_server>
		<element>for_make_array</element>
        <element>for_make_array</element>
<element>
			<name>service_discovery</name>
			<host>http://10.0.1.195:2380;http://10.0.1.196:2380;http://10.0.1.197:2380</host>
			<user>zone_1</user>
			<pwd>zone_1</pwd>
		</element>		
	</etcd_server>

	<redis_service>
		<element>for_make_array</element>
		<element>for_make_array</element>
<element>
			<name>online_servers</name>
			<is_cluster>1</is_cluster>
			<host>10.0.1.180:6379,10.0.1.181:6379,10.0.1.182:6379,10.0.1.183:6379,10.0.1.184:6379,10.0.1.185:6379</host>
			<pwd>zone_1</pwd>
			<thread_num>3</thread_num>
			<cnn_timeout_ms>3000</cnn_timeout_ms>
			<cmd_timeout_ms>3000</cmd_timeout_ms>
		</element>
	</redis_service>

	<mongo_service>
		<element>for_make_array</element>
		<element>for_make_array</element>
<element>
			<name>game</name>
			<host>10.0.1.210:27017</host>
			<auth_db>admin</auth_db>
			<user>lxl</user>
			<pwd>xiaolzz</pwd>
			<thread_num>3</thread_num>
		</element>
	</mongo_service>

	<advertise_peer_ip>10.0.1.187</advertise_peer_ip>
	<advertise_peer_port>100002</advertise_peer_port>
	<advertise_client_ip>10.0.1.187</advertise_client_ip>
	<advertise_client_port>100001</advertise_client_port>
	<advertise_http_ip>127.0.0.1</advertise_http_ip>
	<advertise_http_port>30103</advertise_http_port>
	<platform_http_ip>127.0.0.1</platform_http_ip>
	<platform_http_port>30053</platform_http_port>
</root>


