-- Keep the PDF export readable without changing the Markdown source.

local function replace_export_symbols(text)
  return text
    :gsub("≠", "not equal to")
    :gsub("∈", "in")
    :gsub("├", "|")
    :gsub("└", "|")
    :gsub("─", "-")
end

local function latex_escape(text)
  return text
    :gsub("\\", "\\textbackslash{}")
    :gsub("([%%#$&_{}])", "\\%1")
    :gsub("~", "\\textasciitilde{}")
    :gsub("%^", "\\textasciicircum{}")
end

local function break_long_code(text)
  local has_break_marker = text:find("/", 1, true)
    or text:find("_", 1, true)
    or text:find("-", 1, true)
    or text:find(".", 1, true)
  if #text < 16
    or (
      not text:match("[a-z0-9][A-Z]")
      and not has_break_marker
    )
  then
    return nil
  end

  local chunks = {}
  local start = 1
  for index = 2, #text do
    local previous = text:sub(index - 1, index - 1)
    local current = text:sub(index, index)
    if (previous:match("[a-z0-9]") and current:match("[A-Z]"))
      or previous == "/"
      or previous == "_"
      or previous == "-"
      or previous == "."
    then
      chunks[#chunks + 1] = latex_escape(text:sub(start, index - 1))
      start = index
    end
  end
  chunks[#chunks + 1] = latex_escape(text:sub(start))

  if #chunks == 1 then
    return nil
  end
  return pandoc.RawInline(
    "tex",
    "\\texttt{" .. table.concat(chunks, "}\\allowbreak{}\\texttt{") .. "}"
  )
end

function Str(element)
  element.text = replace_export_symbols(element.text)
  local broken_text = break_long_code(element.text)
  if broken_text then
    return broken_text
  end
  return element
end

function Code(element)
  local text = replace_export_symbols(element.text)
  local broken_code = break_long_code(text)
  if broken_code then
    return broken_code
  end
  element.text = text
  return element
end

function CodeBlock(element)
  element.text = replace_export_symbols(element.text)
  return element
end

function Table(element)
  local column_count = #element.colspecs
  if column_count > 1 then
    local widths = {}
    if column_count == 5 then
      widths = { 0.18, 0.25, 0.22, 0.23, 0.12 }
    elseif column_count == 6 then
      widths = { 0.14, 0.18, 0.17, 0.18, 0.20, 0.13 }
    else
      for index = 1, column_count do
        widths[index] = 1 / column_count
      end
    end
    for index = 1, column_count do
      local specification = element.colspecs[index]
      element.colspecs[index] = { specification[1], widths[index] }
    end
  end
  if column_count >= 5 then
    return {
      pandoc.RawBlock("tex", "\\begingroup\\scriptsize"),
      element,
      pandoc.RawBlock("tex", "\\endgroup"),
    }
  end
  return element
end
