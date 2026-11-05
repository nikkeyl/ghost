export default {
  '*.md': ['prettier --write', 'remark --quiet --frail --no-stdout'],
  '*.{js,ts,json,yaml}': 'prettier --write',
};
