0x0A. Configuration management

Every organization needs to define the ideal configuration of its systems. That ideal configuration, or desired state, is the state in which systems and resources are aligned to support development, network performance, and efficiency.

In short, you want your environment to keep running in a desired state. Configuration management helps you do that.

What is Configuration Management?
Configuration management is an automated process that keeps an organization's systems in a desired state. It helps configure and maintain systems (like hardware and software) and correct issues to ensure that those systems remain in a desired state.

What is the Main Purpose of Configuration Management?
Configuration management ensures a system performs as desired over time, even as changes are made to the system. Organizations often use configuration management to reduce configuration drift and maintain compliance with IT security standards.

Resources
Read or watch:

Intro to Configuration Management
Puppet resource type: file (check “Resource types” for all manifest types in the left menu)
Puppet’s Declarative Language: Modeling Instead of Scripting
Puppet lint
Puppet emacs mode

Note on Versioning
Your Ubuntu 20.04 VM should have Puppet 5.5 preinstalled.

Install puppet
$ apt-get install -y ruby=1:2.7+1 --allow-downgrades
$ apt-get install -y ruby-augeas
$ apt-get install -y ruby-shadow
$ apt-get install -y puppet

Install puppet-lint
$ gem install puppet-lint

Tasks
0. Create a file
1. Install a package
2. Execute a command

Author: @LincolnX2 | sabur,yinus@gmail.com
