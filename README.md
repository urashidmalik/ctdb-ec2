CTDB EC2/VPC VIP support in AWS
====

This project is an extention of CTDB to make it work inside of the AWS cloud.
VIPs will be added as private secondary IPs.

Elastic IP functionality is not implemented right now, but is theoretically possible.



Quickstart
====

* Install and configure CTDB
  * Do not forget to create the `public_addresses` and `nodes` file
  * As VIP you can use any non-claimed private address in your VPC
  * VIPs will be added as secondary IP - [be aware of AWS limitations](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-eni.html#AvailableIpPerENI)
* [Install and configure the Amazon ec2 tools](https://tecadmin.net/setup-amazon-ec2-cli-tools-on-linux/)
* Install the ctdb-ec2 rpm - either build it yourself or fetch it from [me](https://storchris.blum.coffee/thefile.rpm)
* Fill in the variables in the `ec-config` file
  * You can use `ec2-describe-regions` to get the appropriate values for `EC2_URL`
* Start CTDB and monitor the log file for problems
* Check on which node your VIP is with `ctdb ip`

Create your own rpm
====

Please follow Amazon docs for [setting up ec2 tools on a Linux instance](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/SettingUp_CommandLine.html)

On your Linux box, please do the following steps to create a rpm

~~~
$ git clone https://github.com/zeichenanonym/ctdb-ec2.git
$ cd ctdb-ec2/
$ make rpm
~~~

Afterwards you have a rpm file ready for your own use
