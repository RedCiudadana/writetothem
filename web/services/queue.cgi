#!/usr/bin/perl -w -I../../perllib -I../../../perllib
#
# server:
#
# Copyright (c) 2004 UK Citizens Online Democracy. All rights reserved.
# Email: chris@mysociety.org; WWW: http://www.mysociety.org/
#

my $rcsid = ''; $rcsid .= '$Id: queue.cgi,v 1.1 2004-11-10 18:21:09 francis Exp $';

use FCGI;
use FYR;
use FYR::Queue;
use mySociety::DaDem;
use RABX;

use mySociety::Config;
mySociety::Config::set_file('../../conf/general');

use mySociety::WatchUpdate;
my $W = new mySociety::WatchUpdate();

my $req = FCGI::Request();

while ($req->Accept() >= 0) {
    RABX::Server::CGI::dispatch(
            'FYR.Queue.create' => sub {
                return FYR::Queue->create(@_);
            },
            'FYR.Queue.write' => sub {
                return FYR::Queue->write(@_);
            },
            'FYR.Queue.secret' => sub {
                return FYR::Queue->secret(@_);
            },
            'FYR.Queue.confirm_email' => sub {
                return FYR::Queue->confirm_email(@_);
            }
        );
    $W->exit_if_changed();
}



