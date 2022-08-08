# zone Zone
# server GameServer

<?xml version="1.0" encoding="UTF-8"?>
<root>
	<zone>zone_1</zone>
	<server_role>auth</server_role>
	<server_name>zone_1_auth</server_name>

	<etcd_server>
		<element>for_make_array</element>
		<element>for_make_array</element>		
	</etcd_server>

	<redis_service>
		<element>for_make_array</element>
		<element>for_make_array</element>
	</redis_service>

	<mongo_service>
		<element>for_make_array</element>
		<element>for_make_array</element>
		<element>
			<name>uuid</name>
			<host>10.0.1.183:27017</host>
			<auth_db>admin</auth_db>
			<user>lxl</user>
			<pwd>xiaolzz</pwd>
			<thread_num>3</thread_num>
		</element>
		<element>
			<name>auth</name>
			<host>10.0.1.183:27017</host>
			<auth_db>admin</auth_db>
			<user>lxl</user>
			<pwd>xiaolzz</pwd>
			<thread_num>3</thread_num>
		</element>
	</mongo_service>

	<advertise_peer_ip>10.0.1.11</advertise_peer_ip>
	<advertise_peer_port>10002</advertise_peer_port>
	<advertise_client_ip>119.91.239.128</advertise_client_ip>
	<advertise_client_port>41201</advertise_client_port>
	<advertise_http_ip>119.91.239.128</advertise_http_ip>
	<advertise_http_port>41202</advertise_http_port>
    <platform_http_ip>119.91.239.128</platform_http_ip>
    <platform_http_port>41102</platform_http_port>
</root>

