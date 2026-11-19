"""Site-wide icon set for resource cards (experiment on Topic 4, Nov 2026).
Each resource kind has one line icon (24x24, stroke only) and one student purpose:
Learn (read or watch to understand), Practise (do questions or tasks), Explore (use a tool or look at data), Browse (go to a list).
Style matches the 'More resources' heading: a small rounded square in the topic colour with a gold stroke."""
P='<svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="#ffd24a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">%s</svg>'
ICON={
 'Explainer':P%'<path d="M3 5.5C5 4.5 8.5 4.5 12 6.5c3.5-2 7-2 9-1v13c-2-1-5.5-1-9 1-3.5-2-7-2-9-1z"/><path d="M12 6.5v13"/>',
 'Slides':P%'<rect x="3" y="4" width="18" height="12" rx="2"/><path d="M12 16v4M8 20h8"/>',
 'Notes':P%'<path d="M6 3h8l4 4v14H6z"/><path d="M14 3v4h4M9 12h6M9 16h6"/>',
 'Workbook':P%'<rect x="5" y="3" width="14" height="18" rx="2"/><path d="M9 3v18M12 8h4M12 12h4"/>',
 'Worksheet':P%'<rect x="5" y="4" width="14" height="17" rx="2"/><path d="M9 4V3h6v1M8.5 11l1.5 1.5 2.5-3M8.5 17l1.5 1.5 2.5-3M14.5 11.5h2M14.5 17.5h2"/>',
 'Practice':P%'<circle cx="12" cy="12" r="8"/><circle cx="12" cy="12" r="4"/><path d="M12 12l6-6"/>',
 'Tool':P%'<path d="M5 8h8M17 8h2M5 16h2M11 16h8"/><circle cx="15" cy="8" r="2"/><circle cx="9" cy="16" r="2"/>',
 'Chart':P%'<path d="M4 20h16M7 20v-6M12 20V6M17 20v-9"/>',
 'Diagram':P%'<path d="M4 4v16h16"/><path d="M6 8c5 0 8 4 12 10M6 18c5 0 8-4 12-10"/>',
 'Topic page':P%'<rect x="4" y="4" width="7" height="7" rx="1.5"/><rect x="13" y="4" width="7" height="7" rx="1.5"/><rect x="4" y="13" width="7" height="7" rx="1.5"/><rect x="13" y="13" width="7" height="7" rx="1.5"/>',
}
PURPOSE={'Explainer':'Learn','Slides':'Learn','Notes':'Learn','Workbook':'Practise','Worksheet':'Practise','Practice':'Practise','Tool':'Explore','Chart':'Explore','Diagram':'Explore','Topic page':'Browse'}
def tag(kind):
    if kind not in PURPOSE: return kind
    if kind=='Practice': return 'Practise · questions'
    return '%s · %s'%(kind,PURPOSE[kind])
def legend():
    items=[('Explainer','Learn','read or watch to understand'),('Workbook','Practise','questions and tasks'),('Tool','Explore','tools and data')]
    return '<div class="lg">'+''.join('<span><em class="ic">%s</em><b>%s</b> %s</span>'%(ICON[k],p,d) for k,p,d in items)+'</div>'

# extra kinds used on Topics 1-3
ICON['Activity']=ICON['Worksheet']; PURPOSE['Activity']='Practise'
ICON['Case study']=ICON['Notes']; PURPOSE['Case study']='Learn'

# ---- icon set v2 (approved 19 Nov 2026): one set for the site, the workbook and the slides ----
# The ten shapes above are unchanged. These add activity types, "go online" markers and section icons.
# Print versions (navy on cream, and mono) are made by the workbook build from the same shapes.
ICON.update({
 'Watch':P%'<rect x="3" y="5" width="18" height="14" rx="2"/><path d="M10 9l5 3-5 3z"/>',
 'Calculate':P%'<rect x="5" y="3" width="14" height="18" rx="2"/><path d="M8.5 7.5h7M8.6 12h.01M12 12h.01M15.4 12h.01M8.6 16.5h.01M12 16.5h.01M15.4 16.5h.01"/>',
 'Draw':P%'<path d="M4 4v16h16"/><path d="M9 15.5l1-3.5 7.5-7.5 2.5 2.5-7.5 7.5z"/>',
 'Discuss':P%'<path d="M3 5h11v7H8.5L6 14.5V12H3z"/><path d="M17 9h4v7h-2.5v2.5L16 16h-5"/>',
 'Write':P%'<path d="M4 20h7"/><path d="M7 17l1-4 9-9 3 3-9 9z"/><path d="M15 6l3 3"/>',
 'Exam question':P%'<circle cx="12" cy="12" r="9"/><path d="M9.3 9.6a2.8 2.8 0 1 1 4.2 2.4c-1 .6-1.5 1.1-1.5 2.2M12 17.2h.01"/>',
 'Extension':P%'<path d="M12 3l2.7 5.6 6.1.8-4.5 4.2 1.1 6.1L12 16.8 6.6 19.7l1.1-6.1L3.2 9.4l6.1-.8z"/>',
 'Scan':P%'<path d="M4 8V4h4M16 4h4v4M20 16v4h-4M8 20H4v-4"/><rect x="9" y="9" width="6" height="6" rx="1"/>',
 'Live chart':P%'<path d="M4 4v16h16"/><path d="M7 16l3.5-4 3 2.5 3.5-4.5"/><circle cx="19" cy="6" r="1.6"/>',
 'Website':P%'<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c3.2 3 3.2 15 0 18M12 3c-3.2 3-3.2 15 0 18"/>',
 'Trade and financial flows':P%'<path d="M4 8h15M15 4l4 4-4 4"/><path d="M20 16H5M9 12l-4 4 4 4"/>',
 'Balance of payments':P%'<path d="M12 4v16M8 20h8M5 7h14"/><path d="M5 7l-2.5 6a2.5 2.5 0 0 0 5 0zM19 7l-2.5 6a2.5 2.5 0 0 0 5 0z"/>',
 'Exchange rates':P%'<circle cx="12" cy="12" r="9"/><path d="M15 9.3c-.5-1.2-1.6-1.8-3-1.8-1.7 0-3 .9-3 2.2 0 3.1 6 1.5 6 4.7 0 1.4-1.3 2.3-3 2.3-1.5 0-2.7-.7-3.2-1.9M12 5.5v13"/>',
 'External stability':P%'<path d="M12 3l8 3v6c0 4.5-3.3 7.7-8 9-4.700-1.300-8-4.500-8-9V6z"/><path d="M8.5 12l2.5 2.500 4.500-5"/>',
})
ICON['Read']=ICON['Explainer']; ICON['Online tool']=ICON['Tool']; ICON['Online extension']=ICON['Extension']
PURPOSE.update({'Watch':'Learn','Read':'Learn','Calculate':'Practise','Draw':'Practise','Discuss':'Practise','Write':'Practise','Exam question':'Practise',
 'Extension':'Extend','Online extension':'Extend','Live chart':'Explore','Online tool':'Explore','Website':'Browse','Scan':'Browse'})
