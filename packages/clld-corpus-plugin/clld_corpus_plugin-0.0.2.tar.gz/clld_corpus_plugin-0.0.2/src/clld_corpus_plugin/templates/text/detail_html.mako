<%inherit file="../${context.get('request').registry.settings.get('clld.app_template', 'app.mako')}"/>
<%namespace name="util" file="../util.mako"/>
<%import clld_corpus_plugin.util as cutil%>
<link rel="stylesheet" href="${req.static_url('clld_corpus_plugin:static/clld-corpus.css')}"/>
<%! active_menu_item = "texts" %>


<h3>${_('Text')} “${ctx.name}”</h3>
<dl>
    % if ctx.text_metadata:
        % for key, value in ctx.text_metadata.items():
            <dt>${key.capitalize()}</dt> <dd>${value}</dd>
        % endfor
    % endif
    % if ctx.source:
        <dt>Source</dt> <dd>${h.link(request, ctx.source)}</dd>
    % endif
    % if ctx.description:
        <dt>Summary</dt> ${h.text2html(h.Markup(ctx.description))}
    % endif
</dl>

<ol>
% for s in ctx.sentences:
${cutil.rendered_sentence(request, s.sentence, text_link=False, sentence_link=True)}
% endfor
</ol>

<script src="${req.static_url('clld_corpus_plugin:static/clld-corpus.js')}">
</script>

<script>
number_examples()
</script>