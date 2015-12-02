# Copyright 2006-2009 the V8 project authors. All rights reserved.
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met:
#
#     * Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above
#       copyright notice, this list of conditions and the following
#       disclaimer in the documentation and/or other materials provided
#       with the distribution.
#     * Neither the name of Google Inc. nor the names of its
#       contributors may be used to endorse or promote products derived
#       from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

# Dictionary that is passed as defines for js2c.py.
# Used for defines that must be defined for all native JS files.

define NONE        = 0;
define READ_ONLY   = 1;
define DONT_ENUM   = 2;
define DONT_DELETE = 4;
define NEW_ONE_BYTE_STRING = true;
define NEW_TWO_BYTE_STRING = false;

# Constants used for getter and setter operations.
define GETTER = 0;
define SETTER = 1;

# For date.js.
define HoursPerDay      = 24;
define MinutesPerHour   = 60;
define SecondsPerMinute = 60;
define msPerSecond      = 1000;
define msPerMinute      = 60000;
define msPerHour        = 3600000;
define msPerDay         = 86400000;
define msPerMonth       = 2592000000;

# Note: kDayZeroInJulianDay = ToJulianDay(1970, 0, 1).
define kInvalidDate        = 'Invalid Date';
define kDayZeroInJulianDay = 2440588;
define kMonthMask          = 0x1e0;
define kDayMask            = 0x01f;
define kYearShift          = 9;
define kMonthShift         = 5;

# Limits for parts of the date, so that we support all the dates that
# ECMA 262 - 15.9.1.1 requires us to, but at the same time be sure that
# the date (days since 1970) is in SMI range.
define kMinYear  = -1000000;
define kMaxYear  = 1000000;
define kMinMonth = -10000000;
define kMaxMonth = 10000000;

# Safe maximum number of arguments to push to stack, when multiplied by
# pointer size. Used by Function.prototype.apply(), Reflect.apply() and
# Reflect.construct().
define kSafeArgumentsLength = 0x800000;

# 2^53 - 1
define kMaxSafeInteger = 9007199254740991;

# 2^32 - 1
define kMaxUint32 = 4294967295;

# Strict mode flags for passing to %SetProperty
define kSloppyMode = 0;
define kStrictMode = 1;

# Native cache ids.
define STRING_TO_REGEXP_CACHE_ID = 0;

# Type query macros.
#
# Note: We have special support for typeof(foo) === 'bar' in the compiler.
#       It will *not* generate a runtime typeof call for the most important
#       values of 'bar'.
macro IS_NULL(arg)              = (arg === null);
macro IS_NULL_OR_UNDEFINED(arg) = (arg == null);
macro IS_UNDEFINED(arg)         = (arg === (void 0));
macro IS_NUMBER(arg)            = (typeof(arg) === 'number');
macro IS_STRING(arg)            = (typeof(arg) === 'string');
macro IS_BOOLEAN(arg)           = (typeof(arg) === 'boolean');
macro IS_SYMBOL(arg)            = (typeof(arg) === 'symbol');
macro IS_OBJECT(arg)            = (typeof(arg) === 'object');
macro IS_ARRAY(arg)             = (%_IsArray(arg));
macro IS_DATE(arg)              = (%_IsDate(arg));
macro IS_FUNCTION(arg)          = (%_IsFunction(arg));
macro IS_REGEXP(arg)            = (%_IsRegExp(arg));
macro IS_SIMD_VALUE(arg)        = (%_IsSimdValue(arg));
macro IS_SET(arg)               = (%_ClassOf(arg) === 'Set');
macro IS_MAP(arg)               = (%_ClassOf(arg) === 'Map');
macro IS_WEAKMAP(arg)           = (%_ClassOf(arg) === 'WeakMap');
macro IS_WEAKSET(arg)           = (%_ClassOf(arg) === 'WeakSet');
macro IS_NUMBER_WRAPPER(arg)    = (%_ClassOf(arg) === 'Number');
macro IS_STRING_WRAPPER(arg)    = (%_ClassOf(arg) === 'String');
macro IS_SYMBOL_WRAPPER(arg)    = (%_ClassOf(arg) === 'Symbol');
macro IS_BOOLEAN_WRAPPER(arg)   = (%_ClassOf(arg) === 'Boolean');
macro IS_ERROR(arg)             = (%_ClassOf(arg) === 'Error');
macro IS_SCRIPT(arg)            = (%_ClassOf(arg) === 'Script');
macro IS_GLOBAL(arg)            = (%_ClassOf(arg) === 'global');
macro IS_ARRAYBUFFER(arg)       = (%_ClassOf(arg) === 'ArrayBuffer');
macro IS_DATAVIEW(arg)          = (%_ClassOf(arg) === 'DataView');
macro IS_SHAREDARRAYBUFFER(arg) = (%_ClassOf(arg) === 'SharedArrayBuffer');
macro IS_GENERATOR(arg)         = (%_ClassOf(arg) === 'Generator');
macro IS_SET_ITERATOR(arg)      = (%_ClassOf(arg) === 'Set Iterator');
macro IS_MAP_ITERATOR(arg)      = (%_ClassOf(arg) === 'Map Iterator');
macro IS_STRONG(arg)            = (%IsStrong(arg));

# Macro for ECMAScript 5 queries of the type:
# "Type(O) is object."
# This is the same as being either a function or an object in V8 terminology
# (including proxies).
# In addition, an undetectable object is also included by this.
macro IS_SPEC_OBJECT(arg)   = (%_IsJSReceiver(arg));

# Macro for ECMAScript 5 queries of the type:
# "IsCallable(O)"
macro IS_CALLABLE(arg) = (typeof(arg) === 'function');

# Macro for ES6 CheckObjectCoercible
# Will throw a TypeError of the form "[functionName] called on null or undefined".
macro CHECK_OBJECT_COERCIBLE(arg, functionName) = if (IS_NULL(%IS_VAR(arg)) || IS_UNDEFINED(arg)) throw MakeTypeError(kCalledOnNullOrUndefined, functionName);

# Indices in bound function info retrieved by %BoundFunctionGetBindings(...).
define kBoundFunctionIndex = 0;
define kBoundThisIndex = 1;
define kBoundArgumentsStartIndex = 2;

# Inline macros. Use %IS_VAR to make sure arg is evaluated only once.
macro NUMBER_IS_NAN(arg) = (!%_IsSmi(%IS_VAR(arg)) && !(arg == arg));
macro NUMBER_IS_FINITE(arg) = (%_IsSmi(%IS_VAR(arg)) || ((arg == arg) && (arg != 1/0) && (arg != -1/0)));
macro TO_BOOLEAN(arg) = (!!(arg));
macro TO_INTEGER(arg) = (%_ToInteger(arg));
macro TO_INTEGER_MAP_MINUS_ZERO(arg) = (%_IsSmi(%IS_VAR(arg)) ? arg : %NumberToIntegerMapMinusZero(arg));
macro TO_INT32(arg) = ((arg) | 0);
macro TO_UINT32(arg) = ((arg) >>> 0);
macro TO_LENGTH(arg) = (%_ToLength(arg));
macro TO_LENGTH_OR_UINT32(arg) = (FLAG_harmony_tolength ? TO_LENGTH(arg) : TO_UINT32(arg));
macro TO_LENGTH_OR_INTEGER(arg) = (FLAG_harmony_tolength ? TO_LENGTH(arg) : TO_INTEGER(arg));
macro TO_STRING(arg) = (%_ToString(arg));
macro TO_NUMBER(arg) = (%_ToNumber(arg));
macro TO_OBJECT(arg) = (%_ToObject(arg));
macro TO_PRIMITIVE(arg) = (%_ToPrimitive(arg));
macro TO_PRIMITIVE_NUMBER(arg) = (%_ToPrimitive_Number(arg));
macro TO_PRIMITIVE_STRING(arg) = (%_ToPrimitive_String(arg));
macro TO_NAME(arg) = (%_ToName(arg));
macro JSON_NUMBER_TO_STRING(arg) = ((%_IsSmi(%IS_VAR(arg)) || arg - arg == 0) ? %_NumberToString(arg) : "null");
macro HAS_OWN_PROPERTY(arg, index) = (%_Call(ObjectHasOwnProperty, arg, index));
macro HAS_INDEX(array, index, is_array) = ((is_array && %_HasFastPackedElements(%IS_VAR(array))) ? (index < array.length) : (index in array));

# Private names.
macro IS_PRIVATE(sym) = (%SymbolIsPrivate(sym));
macro HAS_PRIVATE(obj, sym) = (%HasOwnProperty(obj, sym));
macro HAS_DEFINED_PRIVATE(obj, sym) = (!IS_UNDEFINED(obj[sym]));
macro GET_PRIVATE(obj, sym) = (obj[sym]);
macro SET_PRIVATE(obj, sym, val) = (obj[sym] = val);

# Constants.  The compiler constant folds them.
define INFINITY = (1/0);
define UNDEFINED = (void 0);

# Macros implemented in Python.
python macro CHAR_CODE(str) = ord(str[1]);

# Constants used on an array to implement the properties of the RegExp object.
define REGEXP_NUMBER_OF_CAPTURES = 0;
define REGEXP_FIRST_CAPTURE = 3;

# Macros for internal slot access.
macro REGEXP_GLOBAL(regexp) = (%_RegExpFlags(regexp) & 1);
macro REGEXP_IGNORE_CASE(regexp) = (%_RegExpFlags(regexp) & 2);
macro REGEXP_MULTILINE(regexp) = (%_RegExpFlags(regexp) & 4);
macro REGEXP_STICKY(regexp) = (%_RegExpFlags(regexp) & 8);
macro REGEXP_UNICODE(regexp) = (%_RegExpFlags(regexp) & 16);
macro REGEXP_SOURCE(regexp) = (%_RegExpSource(regexp));

# We can't put macros in macros so we use constants here.
# REGEXP_NUMBER_OF_CAPTURES
macro NUMBER_OF_CAPTURES(array) = ((array)[0]);

# Limit according to ECMA 262 15.9.1.1
define MAX_TIME_MS = 8640000000000000;
# Limit which is MAX_TIME_MS + msPerMonth.
define MAX_TIME_BEFORE_UTC = 8640002592000000;

# Gets the value of a Date object. If arg is not a Date object
# a type error is thrown.
macro CHECK_DATE(arg) = if (!%_IsDate(arg)) %_ThrowNotDateError();
macro LOCAL_DATE_VALUE(arg) = (%_DateField(arg, 0) + %_DateField(arg, 21));
macro UTC_DATE_VALUE(arg)    = (%_DateField(arg, 0));

macro LOCAL_YEAR(arg)        = (%_DateField(arg, 1));
macro LOCAL_MONTH(arg)       = (%_DateField(arg, 2));
macro LOCAL_DAY(arg)         = (%_DateField(arg, 3));
macro LOCAL_WEEKDAY(arg)     = (%_DateField(arg, 4));
macro LOCAL_HOUR(arg)        = (%_DateField(arg, 5));
macro LOCAL_MIN(arg)         = (%_DateField(arg, 6));
macro LOCAL_SEC(arg)         = (%_DateField(arg, 7));
macro LOCAL_MS(arg)          = (%_DateField(arg, 8));
macro LOCAL_DAYS(arg)        = (%_DateField(arg, 9));
macro LOCAL_TIME_IN_DAY(arg) = (%_DateField(arg, 10));

macro UTC_YEAR(arg)        = (%_DateField(arg, 11));
macro UTC_MONTH(arg)       = (%_DateField(arg, 12));
macro UTC_DAY(arg)         = (%_DateField(arg, 13));
macro UTC_WEEKDAY(arg)     = (%_DateField(arg, 14));
macro UTC_HOUR(arg)        = (%_DateField(arg, 15));
macro UTC_MIN(arg)         = (%_DateField(arg, 16));
macro UTC_SEC(arg)         = (%_DateField(arg, 17));
macro UTC_MS(arg)          = (%_DateField(arg, 18));
macro UTC_DAYS(arg)        = (%_DateField(arg, 19));
macro UTC_TIME_IN_DAY(arg) = (%_DateField(arg, 20));

macro TIMEZONE_OFFSET(arg)   = (%_DateField(arg, 21));

macro SET_UTC_DATE_VALUE(arg, value) = (%DateSetValue(arg, value, 1));
macro SET_LOCAL_DATE_VALUE(arg, value) = (%DateSetValue(arg, value, 0));

# Last input and last subject of regexp matches.
define LAST_SUBJECT_INDEX = 1;
macro LAST_SUBJECT(array) = ((array)[1]);
macro LAST_INPUT(array) = ((array)[2]);

# REGEXP_FIRST_CAPTURE
macro CAPTURE(index) = (3 + (index));
define CAPTURE0 = 3;
define CAPTURE1 = 4;

# For the regexp capture override array.  This has the same
# format as the arguments to a function called from
# String.prototype.replace.
macro OVERRIDE_MATCH(override) = ((override)[0]);
macro OVERRIDE_POS(override) = ((override)[(override).length - 2]);
macro OVERRIDE_SUBJECT(override) = ((override)[(override).length - 1]);
# 1-based so index of 1 returns the first capture
macro OVERRIDE_CAPTURE(override, index) = ((override)[(index)]);

# PropertyDescriptor return value indices - must match
# PropertyDescriptorIndices in runtime-object.cc.
define IS_ACCESSOR_INDEX = 0;
define VALUE_INDEX = 1;
define GETTER_INDEX = 2;
define SETTER_INDEX = 3;
define WRITABLE_INDEX = 4;
define ENUMERABLE_INDEX = 5;
define CONFIGURABLE_INDEX = 6;

# For messages.js
# Matches Script::Type from objects.h
define TYPE_NATIVE = 0;
define TYPE_EXTENSION = 1;
define TYPE_NORMAL = 2;

# Matches Script::CompilationType from objects.h
define COMPILATION_TYPE_HOST = 0;
define COMPILATION_TYPE_EVAL = 1;
define COMPILATION_TYPE_JSON = 2;

# Matches Messages::kNoLineNumberInfo from v8.h
define kNoLineNumberInfo = 0;

# Deprecated, do not use. Will be replaced by PropertyFilter.
define PROPERTY_ATTRIBUTES_STRING = 8;
define PROPERTY_ATTRIBUTES_SYMBOLIC = 16;
define PROPERTY_ATTRIBUTES_PRIVATE_SYMBOL = 32;

# Use for keys, values and entries iterators.
define ITERATOR_KIND_KEYS = 1;
define ITERATOR_KIND_VALUES = 2;
define ITERATOR_KIND_ENTRIES = 3;

macro FIXED_ARRAY_GET(array, index) = (%_FixedArrayGet(array, (index) | 0));
macro FIXED_ARRAY_SET(array, index, value) = (%_FixedArraySet(array, (index) | 0, value));
# TODO(adamk): Find a more robust way to force Smi representation.
macro FIXED_ARRAY_SET_SMI(array, index, value) = (FIXED_ARRAY_SET(array, index, (value) | 0));

macro ORDERED_HASH_TABLE_BUCKET_COUNT(table) = (FIXED_ARRAY_GET(table, 0));
macro ORDERED_HASH_TABLE_ELEMENT_COUNT(table) = (FIXED_ARRAY_GET(table, 1));
macro ORDERED_HASH_TABLE_SET_ELEMENT_COUNT(table, count) = (FIXED_ARRAY_SET_SMI(table, 1, count));
macro ORDERED_HASH_TABLE_DELETED_COUNT(table) = (FIXED_ARRAY_GET(table, 2));
macro ORDERED_HASH_TABLE_SET_DELETED_COUNT(table, count) = (FIXED_ARRAY_SET_SMI(table, 2, count));
macro ORDERED_HASH_TABLE_BUCKET_AT(table, bucket) = (FIXED_ARRAY_GET(table, 3 + (bucket)));
macro ORDERED_HASH_TABLE_SET_BUCKET_AT(table, bucket, entry) = (FIXED_ARRAY_SET(table, 3 + (bucket), entry));

macro ORDERED_HASH_TABLE_HASH_TO_BUCKET(hash, numBuckets) = (hash & ((numBuckets) - 1));

macro ORDERED_HASH_SET_ENTRY_TO_INDEX(entry, numBuckets) = (3 + (numBuckets) + ((entry) << 1));
macro ORDERED_HASH_SET_KEY_AT(table, entry, numBuckets) = (FIXED_ARRAY_GET(table, ORDERED_HASH_SET_ENTRY_TO_INDEX(entry, numBuckets)));
macro ORDERED_HASH_SET_CHAIN_AT(table, entry, numBuckets) = (FIXED_ARRAY_GET(table, ORDERED_HASH_SET_ENTRY_TO_INDEX(entry, numBuckets) + 1));

macro ORDERED_HASH_MAP_ENTRY_TO_INDEX(entry, numBuckets) = (3 + (numBuckets) + ((entry) * 3));
macro ORDERED_HASH_MAP_KEY_AT(table, entry, numBuckets) = (FIXED_ARRAY_GET(table, ORDERED_HASH_MAP_ENTRY_TO_INDEX(entry, numBuckets)));
macro ORDERED_HASH_MAP_VALUE_AT(table, entry, numBuckets) = (FIXED_ARRAY_GET(table, ORDERED_HASH_MAP_ENTRY_TO_INDEX(entry, numBuckets) + 1));
macro ORDERED_HASH_MAP_CHAIN_AT(table, entry, numBuckets) = (FIXED_ARRAY_GET(table, ORDERED_HASH_MAP_ENTRY_TO_INDEX(entry, numBuckets) + 2));

# Must match OrderedHashTable::kNotFound.
define NOT_FOUND = -1;

# Check whether debug is active.
define DEBUG_IS_ACTIVE = (%_DebugIsActive() != 0);
macro DEBUG_PREPARE_STEP_IN_IF_STEPPING(function) = if (%_DebugIsActive() != 0) %DebugPrepareStepInIfStepping(function);

# SharedFlag equivalents
define kNotShared = false;
define kShared = true;
