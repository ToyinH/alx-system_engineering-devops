#!/usr/bin/env bash
# without password, use puppet to connect

file {
  '/etc/ssh/ssh_config':
    ensure => present,
}

file_line {
  'Turn off Password authentication':
    path => '/etc/ssh/ssh_config',
    line => 'PasswordAuthentication no',
    match => '^#PasswordAuthentication',
}

file_line {
  'identity file':
    path => '/etc/ssh/ssh_config',
    line => 'IdentityFile ~/.ssh/school',
    match => '^#IdentityFile',
}
