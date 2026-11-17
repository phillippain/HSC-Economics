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
