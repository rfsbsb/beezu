#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Mitter, a Maemo client for Twitter.
# Copyright (C) 2007, 2008  Julio Biason
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import datetime
import gettext

# ----------------------------------------------------------------------
# I18n bits
# ----------------------------------------------------------------------
t = gettext.translation('timesince', fallback=True)
_ = t.gettext
N_ = t.ngettext

# Adapted (but modified to use ngettext) from
#  http://code.djangoproject.com/browser/django/trunk/django/utils/timesince.py
# My version expects time to be given in UTC & returns timedelta from UTC.

def timesince(timestamp):
    """
    Takes two datetime objects and returns the time between then and now
    as a nicely formatted string, e.g "10 minutes"
    Adapted from http://blog.natbat.co.uk/archive/2003/Jun/14/time_since
    """
    assert(isinstance(timestamp, datetime.datetime))
    chunks = (
        (60 * 60 * 24 * 365, lambda n: N_('year', 'years', n)),
        (60 * 60 * 24 * 30, lambda n: N_('month', 'months', n)),
        (60 * 60 * 24 * 7, lambda n: N_('week', 'weeks', n)),
        (60 * 60 * 24, lambda n: N_('day', 'days', n)),
        (60 * 60, lambda n: N_('hour', 'hours', n)),
        (60, lambda n: N_('minute', 'minutes', n)))

    now = datetime.datetime.utcnow()

    # ignore microsecond part of 'd' since we removed it from 'now'
    delta = now - timestamp
    since = (delta.days * 24 * 60 * 60) + delta.seconds
    if since <= 0:
        return _('just now')

    result = None
    for (seconds, name) in chunks:
        part = since / seconds
        if part < 1:
            continue

        # all divs in Python 2.x are integers; we'll have to check this again
        # when we change to Python 3.
        elapsed = '%s %s' % (part, name(part))
        result = _('%s ago') % (elapsed)
        break

    if not result:
        result = _('less than a minute ago')

    return result
