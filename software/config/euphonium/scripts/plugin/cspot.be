class CSpotPlugin : Plugin
    def init()
        self.apply_default_values()
        self.name = "cspot"
        self.theme_color = "#1DB954"
        self.display_name = "Spotify Connect"
        self.type = "plugin"
    end

    def make_form(ctx, state)
        ctx.create_group('spotify', { 'label': 'General' })

        ctx.text_field('receiverName', {
            'label': "Speaker's name",
            'default': "STRØM 1.0",
            'group': 'spotify'
        })
        ctx.select_field('audioBitrate', {
            'label': "Audio bitrate",
            'default': "320",
            'values': ['320', '160', '96'],
            'group': 'spotify'
        })
        ctx.checkbox_field('overrideAp', {
            'label': "Override access point address",
            'default': "true",
            'group': 'spotify'
        })

        if state.find('overrideAp') != nil && state['overrideAp'] == 'true'
            ctx.text_field('apAddress', {
                'label': "Access point address",
                'default': "ap-gew1.spotify.com:4070",
                'group': 'spotify'
            })
        end
    end

    def on_event(event, data)
        if event == EVENT_SET_PAUSE
            cspot_set_pause(data)
        end

        if event == EVENT_VOLUME_UPDATED
            #cspot_set_volume_remote(data)
        end
    end
end

euphonium.register_plugin(CSpotPlugin())
