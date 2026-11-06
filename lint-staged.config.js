export default {
  '*.md': ['prettier --write', 'remark --quiet --frail --no-stdout'],
  '*.mdc': 'prettier --write',
  '*.{js,ts,json,yaml}': 'prettier --write',
};
