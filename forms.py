"""Forms for playlist app."""

from wtforms import SelectField, StringField
from wtforms.validators import InputRequired, Length, NumberRange, Email, Optional
from flask_wtf import FlaskForm


class PlaylistForm(FlaskForm):
    """Form for adding playlists."""

    # Add the necessary code to use this form
    name = StringField(
        "Name of new playlist",
        validators=[InputRequired(), Length(min=1, max=85)])

    discription = StringField(
        "enter discription",
        validators=[InputRequired(), Length(min=1, max=85)])

class SongForm(FlaskForm):
    """Form for adding songs."""

    title = StringField(
        " Enter Title",
        validators=[InputRequired(), Length(min=1, max=85)])

    artist = StringField(
        " Enter artist",
        validators=[InputRequired(), Length(min=1, max=85)])


# DO NOT MODIFY THIS FORM - EVERYTHING YOU NEED IS HERE
class NewSongForPlaylistForm(FlaskForm):
    """Form for adding a song to playlist."""

    song = SelectField('Song To Add', coerce=int)
