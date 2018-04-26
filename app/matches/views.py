from flask import render_template,flash,url_for,redirect
from flask_login import login_required, current_user #might not be required

from . import matches
from ..models import User, Tutor, Student, followers
from .. import db

@matches.route('/messages')
@login_required
def messages():
	return render_template('matches/messages.html', title="Messages")

@matches.route('/unmatch/<username>')
@login_required
def unmatch(username):
	user = User.query.filter_by(username=username).first()
	if user is None:
		return redirect(url_for('matches.messages'))
	current_user.unfollow(user)
	db.session.commit()
	flash('You have unmatched with {}!'.format(username))
	return redirect(url_for('matches.messages'))
